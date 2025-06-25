<template>
  <div>
    <h1>证书管理</h1>
    <!-- 证书列表展示区域 -->
    <div v-if="certificates.length > 0">
      <table>
        <thead>
          <tr>
            <th>证书名称</th>
            <th>颁发机构</th>
            <th>有效期</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="cert in certificates" :key="cert.id">
            <td>{{ cert.name }}</td>
            <td>{{ cert.issuer }}</td>
            <td>{{ cert.validity }}</td>
            <td>
              <button @click="editCertificate(cert.id)">编辑</button>
              <button @click="deleteCertificate(cert.id)">删除</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-else>
      暂无证书数据
    </div>
    <button @click="showAddDialog = true">添加证书</button>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue'
import { getCertificates } from '@/services/api'

interface Certificate {
  id: string
  name: string
  issuer: string
  validity: string
}

export default defineComponent({
  name: 'CertificateList',
  setup() {
    const certificates = ref<Certificate[]>([])
    const showAddDialog = ref(false)

    const fetchCertificates = async () => {
      try {
        const response = await getCertificates()
        certificates.value = response.data
      } catch (error) {
        console.error('获取证书列表失败:', error)
      }
    }

    const editCertificate = (id: string) => {
      // 编辑逻辑
    }

    const deleteCertificate = (id: string) => {
      // 删除逻辑
    }

    fetchCertificates()

    return {
      certificates,
      showAddDialog,
      editCertificate,
      deleteCertificate
    }
  }
})
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}
</style>