// CatPawOpen Dynamic Loader
// 这里的代码会在播放器端执行
// 使用 fetch 加载同目录下的配置文件

(async function() {
    // 动态获取当前配置
    // 假设播放器会将相对路径解析为当前订阅 URL 的同级目录
    const configUrl = './tvbox_config.json'; 
    
    try {
        const response = await fetch(configUrl);
        const config = await response.json();
        
        // 可在此处动态修改配置，例如替换 token 或域名
        // config.spider = ...
        
        return config;
    } catch (e) {
        console.error("Failed to load config:", e);
        return {
            "sites": [],
            "lives": [],
            "spider": ""
        };
    }
})();
