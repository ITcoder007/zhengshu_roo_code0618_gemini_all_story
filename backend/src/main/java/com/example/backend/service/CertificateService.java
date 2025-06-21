package com.example.backend.service;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.backend.domain.Certificate;
import com.example.backend.repository.CertificateRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.List;

@Service
public class CertificateService extends ServiceImpl<CertificateRepository, Certificate> {
    
    public List<Certificate> findByDomain(String domain) {
        QueryWrapper<Certificate> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq("domain", domain);
        return this.list(queryWrapper);
    }

    public boolean updateCertificateStatus(Long id, String status) {
        Certificate certificate = new Certificate();
        certificate.setId(id);
        certificate.setStatus(status);
        return this.updateById(certificate);
    }

    public List<Certificate> findExpiringCertificates(LocalDateTime beforeDate) {
        QueryWrapper<Certificate> queryWrapper = new QueryWrapper<>();
        queryWrapper.lt("expiry_date", beforeDate);
        return this.list(queryWrapper);
    }
}