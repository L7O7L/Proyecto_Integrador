package com.proyecto_integrador.registro_user;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class Register_user {

	@GetMapping("/")
	public String Form_register_user() {
		
		return "Form_register_user";
		
	}
	
}
