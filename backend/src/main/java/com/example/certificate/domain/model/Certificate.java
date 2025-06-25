package com.example.certificate.domain.model;

import com.baomidou.mybatisplus.annotation.*;
import lombok.Data;

import java.time.LocalDate;
import java.time.LocalDateTime;

@Data
@TableName("certificates")
public class Certificate {
    @TableId(type = IdType.AUTO)
    private Long id;
    
    private String domain;
    
    private LocalDate expiryDate;
    
    private String creator;
    
    @TableField(fill = FieldFill.INSERT)
    private LocalDateTime createdAt;
    
    private String modifier;
    
    @TableField(fill = FieldFill.INSERT_UPDATE)
    private LocalDateTime modifiedAt;
}