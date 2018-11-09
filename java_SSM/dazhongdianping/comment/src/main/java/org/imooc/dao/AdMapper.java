package org.imooc.dao;

import java.util.List;
import org.imooc.bean.Ad;

public interface AdMapper {
    int deleteByPrimaryKey(Integer id);

    int insert(Ad record);

    Ad selectByPrimaryKey(Integer id);

    List<Ad> selectAll();

    int updateByPrimaryKey(Ad record);
}