## 依赖

```
opkg install openssl-util  ipset dnsmasq-full diffutils iptables-mod-nat-extra wget ca-bundle ca-certificates libustream-openssl
```

- **openssl**: https过滤模式, 证书生成
- **ipset(6) dnsmasq-full diffutils(or busybox(diff))**: 黑名单模式
- **iptables-mod-nat-extra**: mac过滤模式
- **wget, ca-bundle, ca-certificates, libustream-openssl**: 规则文件更新

## Thanks

- https://github.com/openwrt-develop/luci-app-koolproxy
