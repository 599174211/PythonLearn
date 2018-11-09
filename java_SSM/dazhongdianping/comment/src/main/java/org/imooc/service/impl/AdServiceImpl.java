package org.imooc.service.impl;

import java.io.File;
import java.io.IOException;

import org.imooc.bean.Ad;
import org.imooc.bean.dto.AdDto;
import org.imooc.dao.AdMapper;
import org.imooc.service.AdService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
@Service
public class AdServiceImpl implements AdService {
	
	@Autowired
	private AdMapper adDao;
	
	@Value("${adImage.savePath}")
	private String adImageSavePath;
	@Value("${jdbc.jdbcUrl}")
	private String jdbcUrl;
	@Value("${jdbc.user}")
	private String user;
	@Value("${jdbc.password}")
	private String password;
	
	@Override
	public boolean add(AdDto adDto) {
		// TODO Auto-generated method stub
		Ad ad = new Ad();
		ad.setTitle(adDto.getTitle());
		ad.setLink(adDto.getLink());
		ad.setWeight(adDto.getWeight());
		System.out.println("password:"+password + ",user:" +user + ",jdbcUrl:" +jdbcUrl);
		if(adDto.getImgFile() !=null && adDto.getImgFile().getSize() > 0) {		
			String fileName = System.currentTimeMillis() + "_" + adDto.getImgFile().getOriginalFilename();
			//存的文件路径
			File file = new File(adImageSavePath + fileName);
			File fileFolder = new File(adImageSavePath);
			if(!fileFolder.exists()) {
				fileFolder.mkdirs();
			}
			try {
				adDto.getImgFile().transferTo(file);
				ad.setImgFileName(fileName);
				adDao.insert(ad)		;
				return true;
			} catch (IllegalStateException | IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				return false;
			} 
		}else {
			return false;
		}
	}

}
