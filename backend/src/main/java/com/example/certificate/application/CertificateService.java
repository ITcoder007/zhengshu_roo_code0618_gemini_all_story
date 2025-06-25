package com.example.certificate.application;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.example.certificate.domain.model.Certificate;

public interface CertificateService {
    Certificate createCertificate(Certificate certificate);
    
    Certificate getCertificateById(Long id);
    
    IPage<Certificate> listCertificates(IPage<Certificate> page);
    
    Certificate updateCertificate(Long id, Certificate certificate);
    
    void deleteCertificate(Long id);
}