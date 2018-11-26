package org.imooc.controller.content;

import ch.qos.logback.classic.Logger;
import org.imooc.bean.dto.AdDto;
import org.imooc.constant.PageCodeEnum;
import org.imooc.service.AdService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;


@Controller
@RequestMapping(value="/ad")
public class AdController {
    
	@Autowired
	private AdService adService;
	@RequestMapping
	public String init() {
		return ("/content/adList");
	}
	
	@RequestMapping(value="/addInit")
	public String addInit() {
		return ("/content/adAdd");
	}
	
	@RequestMapping(value="/add")
	public String add(AdDto adDto) {
		adService.add(adDto);
		ModelAndView modelAndView = new ModelAndView();
		return "/content/adAdd";
	}

}
