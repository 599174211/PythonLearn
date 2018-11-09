package org.imooc.bean;

import java.util.List;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonInclude.Include;

@JsonInclude(Include.NON_NULL)
public class CommentList {
	
	private boolean hasMore;
	private List<Comment> data;
	
	public boolean isHasMore() {
		return hasMore;
	}
	public void setHasMore(boolean hasMore) {
		this.hasMore = hasMore;
	}
	public List<Comment> getData() {
	    return data;
	}
	public void setData(List<Comment> data) {
	    this.data = data;
	}
}