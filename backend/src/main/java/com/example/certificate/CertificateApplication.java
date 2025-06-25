package com.example.certificate;

import org.springframework.boot.Banner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ConfigurableApplicationContext;
import org.springframework.core.env.Environment;

@SpringBootApplication
public class CertificateApplication {
    public static void main(String[] args) {
        SpringApplication app = new SpringApplication(CertificateApplication.class);
        app.setBannerMode(Banner.Mode.OFF);
        ConfigurableApplicationContext context = app.run(args);
        
        Environment env = context.getEnvironment();
        String contextPath = env.getProperty("server.servlet.context-path");
        String port = env.getProperty("server.port");
        
        System.out.println("Application started with:");
        System.out.println("Context Path: " + contextPath);
        System.out.println("Port: " + port);
    }
}