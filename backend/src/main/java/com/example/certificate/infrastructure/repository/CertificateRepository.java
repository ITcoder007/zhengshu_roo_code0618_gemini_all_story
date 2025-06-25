package com.example.certificate.infrastructure.repository;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.certificate.domain.model.Certificate;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface CertificateRepository extends BaseMapper<Certificate> {
}