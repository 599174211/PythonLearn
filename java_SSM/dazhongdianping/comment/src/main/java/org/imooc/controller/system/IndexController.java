package org.imooc.controller.system;

import org.omg.CosNaming.NamingContextExtPackage.StringNameHelper;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import java.lang.reflect.MalformedParameterizedTypeException;
import java.util.HashMap;
import java.util.Map;

@Controller
@RequestMapping(value = "/index")
public class IndexController {

    @RequestMapping()
    public String init() {
        return ("/system/index");
    }

    @RequestMapping(value = "index2")
    @ResponseBody
    public Map<String,String> testRest(){
        Map<String, String> mapStr = new HashMap<String, String>();
        mapStr.put("name", "aa");
        return mapStr;
    }
}
