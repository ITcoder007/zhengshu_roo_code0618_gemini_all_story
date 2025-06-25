package com.example.certificate.interfaces;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.example.certificate.application.CertificateService;
import com.example.certificate.domain.model.Certificate;
import com.example.certificate.interfaces.dto.Result;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/certificates")
public class CertificateController {

    private final CertificateService certificateService;

    public CertificateController(CertificateService certificateService) {
        this.certificateService = certificateService;
    }

    @PostMapping
    public Result<Certificate> createCertificate(@RequestBody Certificate certificate) {
        Certificate created = certificateService.createCertificate(certificate);
        return Result.success(created);
    }

    @GetMapping
    public Result<IPage<Certificate>> listCertificates(
            @RequestParam(defaultValue = "1") int page,
            @RequestParam(defaultValue = "10") int size) {
        IPage<Certificate> result = certificateService.listCertificates(new com.baomidou.mybatisplus.extension.plugins.pagination.Page<>(page, size));
        return Result.success(result);
    }

    @GetMapping("/{id}")
    public Result<Certificate> getCertificate(@PathVariable Long id) {
        Certificate certificate = certificateService.getCertificateById(id);
        return Result.success(certificate);
    }

    @PutMapping("/{id}")
    public Result<Certificate> updateCertificate(
            @PathVariable Long id, 
            @RequestBody Certificate certificate) {
        Certificate updated = certificateService.updateCertificate(id, certificate);
        return Result.success(updated);
    }

    @DeleteMapping("/{id}")
    public Result<String> deleteCertificate(@PathVariable Long id) {
        certificateService.deleteCertificate(id);
        return Result.success("删除成功");
    }
}