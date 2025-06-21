package com.example.backend.repository;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.example.backend.domain.Certificate;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface CertificateRepository extends BaseMapper<Certificate> {
}