package org.imooc.service;

import org.imooc.bean.dto.AdDto;

public interface AdService {
	
	/**
	 * 新增广告
	 * @param adDto
	 * @return 是否新增广告: true:成功,false:失败
	 */
	boolean add(AdDto adDto);
}
