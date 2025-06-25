package com.example.certificate.infrastructure.service;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.example.certificate.application.CertificateService;
import com.example.certificate.domain.model.Certificate;
import com.example.certificate.infrastructure.repository.CertificateRepository;
import org.springframework.stereotype.Service;

@Service
public class CertificateServiceImpl extends ServiceImpl<CertificateRepository, Certificate> implements CertificateService {

    @Override
    public Certificate createCertificate(Certificate certificate) {
        save(certificate);
        return certificate;
    }

    @Override
    public Certificate getCertificateById(Long id) {
        return getById(id);
    }

    @Override
    public IPage<Certificate> listCertificates(IPage<Certificate> page) {
        return page(page);
    }

    @Override
    public Certificate updateCertificate(Long id, Certificate certificate) {
        certificate.setId(id);
        updateById(certificate);
        return certificate;
    }

    @Override
    public void deleteCertificate(Long id) {
        removeById(id);
    }
}