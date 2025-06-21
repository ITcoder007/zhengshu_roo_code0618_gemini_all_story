package com.example.backend;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class BackendApplicationTests {

    @Test
    void contextLoads() {
        assertTrue(true);
    }

    @Test
    void exampleTest() {
        assertEquals(2, 1 + 1);
    }
}