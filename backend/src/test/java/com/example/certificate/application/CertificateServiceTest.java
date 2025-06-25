package com.example.certificate.application;

import com.example.certificate.domain.model.Certificate;
import com.example.certificate.infrastructure.repository.CertificateRepository;
import com.example.certificate.infrastructure.service.CertificateServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
public class CertificateServiceTest {

    @Mock
    private CertificateRepository certificateRepository;

    @InjectMocks
    private CertificateServiceImpl certificateService;

    private Certificate testCertificate;

    @BeforeEach
    public void setUp() {
        testCertificate = new Certificate();
        testCertificate.setId(1L);
        testCertificate.setDomain("example.com");
        testCertificate.setExpiryDate(LocalDate.now().plusDays(30));
    }

    @Test
    public void testCreateCertificate() {
        when(certificateRepository.insert(testCertificate)).thenReturn(1);
        
        boolean result = certificateService.save(testCertificate);
        assertTrue(result);
        assertEquals("example.com", testCertificate.getDomain());
        
        verify(certificateRepository, times(1)).insert(testCertificate);
    }

    @Test
    public void testGetCertificateById() {
        when(certificateRepository.selectById(1L)).thenReturn(testCertificate);
        
        Certificate found = certificateService.getById(1L);
        assertNotNull(found);
        assertEquals("example.com", found.getDomain());
        
        verify(certificateRepository, times(1)).selectById(1L);
    }

    @Test
    public void testGetCertificateByIdNotFound() {
        when(certificateRepository.selectById(2L)).thenReturn(null);
        
        Certificate found = certificateService.getById(2L);
        assertNull(found);
        
        verify(certificateRepository, times(1)).selectById(2L);
    }
}