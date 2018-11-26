package org.imooc.service.impl;

import org.imooc.bean.Ad;
import org.imooc.bean.dto.AdDto;
import org.imooc.dao.AdMapper;
import org.imooc.service.AdService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;

@Service
public class AdServiceImpl implements AdService {
	
	@Autowired
	private AdMapper adDao;
	
	@Value("${adImage.savePath}")
	private String adImageSavePath;
	//以后修改
	public boolean add(AdDto adDto) {
		// TODO Auto-generated method stub
		Ad ad = new Ad();
		ad.setTitle(adDto.getTitle());
		ad.setLink(adDto.getLink());
		ad.setWeight(adDto.getWeight());
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
			} catch (IllegalStateException) {
				// TODO Auto-generated catch block
				e.printStackTrace();
				return false;
			} catch (IOException e){
				//TODO 以后加日志
				return false;
			}
		}else {
			return false;
		}
	}
}
