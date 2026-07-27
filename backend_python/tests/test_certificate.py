"""证书接口端到端测试（基于 TestClient + SQLite 内存库）。"""
from datetime import date


def _create(client, domain="example.com", expiry="2027-12-31", creator="tester", modifier="tester"):
    resp = client.post(
        "/api/certificates",
        json={"domain": domain, "expiryDate": expiry, "creator": creator, "modifier": modifier},
    )
    assert resp.status_code == 200, resp.text
    return resp.json()


def test_create_returns_result_envelope(client):
    body = _create(client)
    assert body["code"] == 200
    assert body["message"] == "成功"
    data = body["data"]
    assert data["domain"] == "example.com"
    assert data["expiryDate"] == "2027-12-31"
    assert data["creator"] == "tester"
    assert data["createdAt"] and data["modifiedAt"]
    assert "id" in data


def test_get_by_id(client):
    created = _create(client)["data"]
    resp = client.get(f"/api/certificates/{created['id']}")
    assert resp.status_code == 200
    assert resp.json()["data"]["domain"] == created["domain"]


def test_get_nonexistent_returns_null_data(client):
    # 对齐 Java 版：不存在的 id 返回 data:null
    resp = client.get("/api/certificates/9999")
    assert resp.status_code == 200
    assert resp.json()["data"] is None


def test_list_pagination_shape(client):
    for i in range(3):
        _create(client, domain=f"d{i}.com")
    resp = client.get("/api/certificates?page=1&size=2")
    body = resp.json()["data"]
    assert body["current"] == 1
    assert body["size"] == 2
    assert body["total"] == 3  # Java 版此处恒为 0，Python 版已修正
    assert body["pages"] == 2
    assert len(body["records"]) == 2


def test_update_certificate(client):
    created = _create(client)["data"]
    resp = client.put(
        f"/api/certificates/{created['id']}",
        json={"domain": "updated.com", "expiryDate": "2028-01-01", "modifier": "admin"},
    )
    assert resp.status_code == 200
    data = resp.json()["data"]
    assert data["domain"] == "updated.com"
    assert data["expiryDate"] == "2028-01-01"
    assert data["modifier"] == "admin"


def test_update_nonexistent_returns_404(client):
    resp = client.put("/api/certificates/9999", json={"domain": "x.com"})
    assert resp.status_code == 404


def test_delete_certificate(client):
    created = _create(client)["data"]
    resp = client.delete(f"/api/certificates/{created['id']}")
    assert resp.status_code == 200
    assert resp.json()["message"] == "删除成功"
    # 删除后再查应为 null
    assert client.get(f"/api/certificates/{created['id']}").json()["data"] is None


def test_delete_nonexistent_returns_404(client):
    assert client.delete("/api/certificates/9999").status_code == 404


def test_duplicate_domain_conflict(client):
    _create(client, domain="dup.com")
    resp = client.post("/api/certificates", json={"domain": "dup.com", "expiryDate": "2027-01-01"})
    assert resp.status_code in (409, 500)  # 唯一约束冲突


def test_health(client):
    resp = client.get("/api/health")
    assert resp.status_code == 200
    assert resp.json()["data"]["status"] == "UP"
