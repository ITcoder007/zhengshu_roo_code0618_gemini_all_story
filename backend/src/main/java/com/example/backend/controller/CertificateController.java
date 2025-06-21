package com.example.backend.controller;

import com.example.backend.domain.Certificate;
import com.example.backend.service.CertificateService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDateTime;
import java.util.List;

@RestController
@RequestMapping("/api/certificates")
@Tag(name = "证书管理", description = "证书管理相关API")
public class CertificateController {

    private final CertificateService certificateService;

    public CertificateController(CertificateService certificateService) {
        this.certificateService = certificateService;
    }

    @GetMapping
    @Operation(summary = "获取所有证书", description = "返回系统中所有的证书列表")
    public List<Certificate> getAllCertificates() {
        return certificateService.list();
    }

    @GetMapping("/{id}")
    @Operation(summary = "根据ID获取证书", description = "根据证书ID获取单个证书详情")
    public Certificate getCertificateById(
            @Parameter(description = "证书ID", required = true)
            @PathVariable Long id) {
        return certificateService.getById(id);
    }

    @PostMapping
    @Operation(summary = "创建证书", description = "创建新的证书记录")
    public boolean createCertificate(
            @Parameter(description = "证书信息", required = true)
            @RequestBody Certificate certificate) {
        return certificateService.save(certificate);
    }

    @PutMapping("/{id}")
    @Operation(summary = "更新证书", description = "根据ID更新证书信息")
    public boolean updateCertificate(
            @Parameter(description = "证书ID", required = true)
            @PathVariable Long id,
            @Parameter(description = "更新后的证书信息", required = true)
            @RequestBody Certificate certificate) {
        certificate.setId(id);
        return certificateService.updateById(certificate);
    }

    @GetMapping("/domain/{domain}")
    @Operation(summary = "根据域名查询证书", description = "返回指定域名下的所有证书")
    public List<Certificate> getCertificatesByDomain(
            @Parameter(description = "域名", required = true)
            @PathVariable String domain) {
        return certificateService.findByDomain(domain);
    }

    @GetMapping("/expiring")
    @Operation(summary = "查询即将过期的证书", description = "返回指定日期前即将过期的证书列表")
    public List<Certificate> getExpiringCertificates(
            @Parameter(description = "过期截止日期", required = true)
            @RequestParam LocalDateTime before) {
        return certificateService.findExpiringCertificates(before);
    }
}