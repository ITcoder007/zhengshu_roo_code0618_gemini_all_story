package com.example.backend.domain;

import com.baomidou.mybatisplus.annotation.*;
import io.swagger.v3.oas.annotations.media.Schema;
import lombok.Data;
import java.time.LocalDateTime;

@Data
@TableName("certificate")
@Schema(description = "证书实体")
public class Certificate {
    @TableId(type = IdType.AUTO)
    @Schema(description = "证书唯一标识", example = "1")
    private Long id;
    
    @TableField("domain")
    @Schema(description = "证书绑定的域名", example = "example.com")
    private String domain;
    
    @TableField("issuer")
    @Schema(description = "证书颁发机构", example = "Let's Encrypt")
    private String issuer;
    
    @TableField("expiry_date")
    @Schema(description = "证书过期时间", example = "2025-12-31T23:59:59")
    private LocalDateTime expiryDate;
    
    @TableField("status")
    @Schema(description = "证书状态", example = "VALID", allowableValues = {"VALID", "EXPIRED", "REVOKED"})
    private String status;
    
}