// function Banner() {
//     console.log('hello');
//     this.person = 'xiaowang'
// }
// Banner.prototype.getBanner = function(word){
//     console.log(word);
// };
// var banner = new Banner();
// console.log(banner.person);
// banner.getBanner('nihaoa');

function Banner() {
    this.bannerGroup = $("#banner-group");
    this.index = 1;
    this.leftArrow = $("#left-arrow");
    this.rightArrow= $("#right-arrow");
    this.bannerUl = $("#banner-ul");
    this.bannerulWidth = 798;
    this.bannerList = this.bannerUl.children("li");
    this.bannerCount = this.bannerList.length;
    this.pageControl = $(".page-control");
}

/**
 * 初始化banner
 */
Banner.prototype.initBanner= function(){
    var self = this;
    var fristBanner = self.bannerList.eq(0).clone();
    var lastBanner = self.bannerList.eq(self.bannerCount -1 ).clone();
    self.bannerUl.append(fristBanner);
    self.bannerUl.prepend(lastBanner);
    self.bannerUl.css({"width": self.bannerulWidth * (self.bannerCount + 2),
       "left": -self.bannerulWidth})
};

/**
 * 是指小圆点控制器
 */
Banner.prototype.initPageControl = function(){
    var self = this;
    for(i = 0; i < this.bannerCount; i++){
        var circle = $("<li></li>");
        self.pageControl.append(circle);
        if(i === 0){
            circle.addClass("active");
        }
    }
    self.pageControl.css({"width": self.bannerCount * 12 + 10 * 2 + (self.bannerCount-1) * 20});
};

/**
 * 监听原点控制器
 */
Banner.prototype.listenPageControl = function(){
    var self = this;
    self.pageControl.children("li").each(function (index, obj) {
        $(obj).click(function () {
            self.index = index + 1;
            self.animate();
        })
    })
};

/**
 * 执行轮播图的动画
 */
Banner.prototype.animate= function(){
    var self = this;
    self.bannerUl.animate({"left": -798 * self.index}, 500);
    var index = self.index;
    if(index === 0){
        index = self.bannerCount - 1;
    }else if (index === self.bannerCount + 1){
        index = 0;
    }else {
        index = self.index - 1;
    }
    self.pageControl.children("li").eq(index)
        .addClass("active").siblings().removeClass("active");

};
/**
 * 控制左右两个箭头的隐藏
 */
Banner.prototype.toggleArrow = function(isShow){

    if(isShow){
        this.leftArrow.show();
        this.rightArrow.show();
    }else {
        this.leftArrow.hide();
        this.rightArrow.hide();
    }
};
/**
 * 左右按钮的监听事件
 */
Banner.prototype.listenArrowClick= function(){
    var self = this;
    self.leftArrow.click(function () {
        if(self.index === 0){
            self.bannerUl.css({"left": -self.bannerulWidth * self.bannerCount});
            self.index = self.bannerCount - 1;
        }else {
            self.index--;
        }
        self.animate();
    });
    self.rightArrow.click(function () {
        if(self.index === (self.bannerCount + 1)){
            self.bannerUl.css({"left": -self.bannerulWidth});
            self.index = 2;
        }else {
            self.index++;
        }
        self.animate();
    });
};
/**
 * 鼠标控制轮播图
 */
Banner.prototype.listenBannerHover = function(){
    var self = this;
    this.bannerGroup.hover(function () {
        //第一个函数表示把鼠标放在bannerGroup上面会执行
        clearInterval(self.timer);
        self.toggleArrow(true);
    }, function () {
      //第二个函数表示把鼠标从bannerGroup上面移走会执行
        self.loop();
        self.toggleArrow(false);
    });
};

/**
 * 循环播放轮播图
 */
Banner.prototype.loop = function(){
    var self = this;
    this.timer =  setInterval(function () {
        if(self.index >= (self.bannerCount + 1) ){
            self.bannerUl.css({"left": -self.bannerulWidth});
            self.index = 2;
        }else {
          self.index ++;
        }
        self.animate();
    },2000);
};
/**
 * 运行loop
 */
Banner.prototype.run = function () {
    this.loop();
    this.listenBannerHover();
    this.listenArrowClick();
    this.initPageControl();
    this.initBanner();
$(function () {
   var banner = new Banner();
   banner.run();
});
    this.listenPageControl();
};

