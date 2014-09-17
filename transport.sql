/*
 Navicat MySQL Data Transfer

 Source Server         : localhost
 Source Server Version : 50163
 Source Host           : localhost
 Source Database       : transport

 Target Server Version : 50163
 File Encoding         : utf-8

 Date: 09/09/2014 22:04:56 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `auth_permission`
-- ----------------------------
BEGIN;
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry'), ('2', 'Can change log entry', '1', 'change_logentry'), ('3', 'Can delete log entry', '1', 'delete_logentry'), ('4', 'Can add permission', '2', 'add_permission'), ('5', 'Can change permission', '2', 'change_permission'), ('6', 'Can delete permission', '2', 'delete_permission'), ('7', 'Can add group', '3', 'add_group'), ('8', 'Can change group', '3', 'change_group'), ('9', 'Can delete group', '3', 'delete_group'), ('10', 'Can add user', '4', 'add_user'), ('11', 'Can change user', '4', 'change_user'), ('12', 'Can delete user', '4', 'delete_user'), ('13', 'Can add content type', '5', 'add_contenttype'), ('14', 'Can change content type', '5', 'change_contenttype'), ('15', 'Can delete content type', '5', 'delete_contenttype'), ('16', 'Can add session', '6', 'add_session'), ('17', 'Can change session', '6', 'change_session'), ('18', 'Can delete session', '6', 'delete_session'), ('19', 'Can add 发货企业', '7', 'add_client'), ('20', 'Can change 发货企业', '7', 'change_client'), ('21', 'Can delete 发货企业', '7', 'delete_client'), ('22', 'Can add 货车司机', '8', 'add_driver'), ('23', 'Can change 货车司机', '8', 'change_driver'), ('24', 'Can delete 货车司机', '8', 'delete_driver'), ('25', 'Can add 订单', '9', 'add_order'), ('26', 'Can change 订单', '9', 'change_order'), ('27', 'Can delete 订单', '9', 'delete_order'), ('28', 'Can add 订单报价', '10', 'add_offer'), ('29', 'Can change 订单报价', '10', 'change_offer'), ('30', 'Can delete 订单报价', '10', 'delete_offer'), ('31', 'Can add 位置信息', '11', 'add_location'), ('32', 'Can change 位置信息', '11', 'change_location'), ('33', 'Can delete 位置信息', '11', 'delete_location'), ('34', 'Can add 货车类型管理', '12', 'add_truck'), ('35', 'Can change 货车类型管理', '12', 'change_truck'), ('36', 'Can delete 货车类型管理', '12', 'delete_truck'), ('37', 'Can add 司机在线位置', '13', 'add_online'), ('38', 'Can change 司机在线位置', '13', 'change_online'), ('39', 'Can delete 司机在线位置', '13', 'delete_online'), ('40', 'Can add 推送记录', '14', 'add_push'), ('41', 'Can change 推送记录', '14', 'change_push'), ('42', 'Can delete 推送记录', '14', 'delete_push');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `auth_user`
-- ----------------------------
BEGIN;
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$12000$lHrj0rnsY3Mv$iEj+E1/o2P44s1neeAeJ2GSZ3x3xit8DuD4E1B0afvA=', '2014-09-04 17:29:58', '1', 'congyuandong', '远东', '丛', 'congyuandong@gmail.com', '1', '1', '2014-08-15 13:15:08');
COMMIT;

-- ----------------------------
--  Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `django_admin_log`
-- ----------------------------
BEGIN;
INSERT INTO `django_admin_log` VALUES ('1', '2014-08-15 13:17:04', '1', '4', '1', 'congyuandong', '2', '已修改 first_name 和 last_name 。'), ('2', '2014-08-16 14:20:56', '1', '8', '1', '丛远东', '1', ''), ('3', '2014-08-19 14:24:56', '1', '8', '6', '11', '3', ''), ('4', '2014-08-19 14:24:56', '1', '8', '5', '11', '3', ''), ('5', '2014-08-19 14:24:56', '1', '8', '4', '11', '3', ''), ('6', '2014-08-19 14:24:56', '1', '8', '3', '11', '3', ''), ('7', '2014-08-24 03:39:56', '1', '9', '1', '2008012345', '1', ''), ('8', '2014-08-24 05:43:07', '1', '7', '1', '1', '3', ''), ('9', '2014-08-24 05:55:46', '1', '9', '1', '11', '1', ''), ('10', '2014-08-24 06:36:48', '1', '9', '1', '12345678', '1', ''), ('11', '2014-08-24 13:00:44', '1', '10', '1', '12345678', '1', ''), ('12', '2014-08-26 07:37:20', '1', '8', '8', '刘启超', '2', '已修改 dr_name，dr_iden，dr_tel，dr_number，dr_hand，dr_type，dr_length，dr_weight 和 dr_pwd 。'), ('13', '2014-08-26 07:43:49', '1', '10', '6', '至诚迅达', '1', ''), ('14', '2014-08-26 07:44:05', '1', '10', '7', '至诚迅达', '1', ''), ('15', '2014-08-26 07:44:23', '1', '10', '8', '至诚迅达', '1', ''), ('16', '2014-08-26 08:50:43', '1', '10', '8', '至诚迅达', '2', '已修改 of_distance 。'), ('17', '2014-08-26 12:07:41', '1', '10', '6', '至诚迅达', '2', '已修改 of_confirm 。'), ('18', '2014-08-26 12:08:55', '1', '9', '1', '黑龙江私营工厂寻找货运物流', '2', '已修改 or_status 。'), ('19', '2014-08-26 12:16:12', '1', '8', '7', '丛远东1', '2', '已修改 dr_name 。'), ('20', '2014-08-26 12:16:49', '1', '8', '2', '丛远东2', '2', '已修改 dr_name 和 dr_tel 。'), ('21', '2014-08-26 12:16:54', '1', '8', '8', '刘启超', '2', '已修改 dr_tel 。'), ('22', '2014-08-26 12:17:01', '1', '8', '1', '丛远东3', '2', '已修改 dr_name 和 dr_iden 。'), ('23', '2014-08-27 11:37:34', '1', '11', '2', 'location object', '2', '已修改 lo_update 。'), ('24', '2014-08-27 11:37:39', '1', '11', '1', 'location object', '2', '已修改 lo_update 。'), ('25', '2014-08-27 11:37:57', '1', '11', '1', 'location object', '2', '已修改 lo_update 。'), ('26', '2014-08-27 11:38:06', '1', '11', '2', 'location object', '2', '已修改 lo_update 。'), ('27', '2014-08-27 12:03:03', '1', '9', '2', '黑龙江私营工厂寻找货运物流', '2', '已修改 or_status 。'), ('28', '2014-08-27 12:03:09', '1', '9', '1', '黑龙江私营工厂寻找货运物流', '2', '已修改 or_status 。'), ('29', '2014-08-27 14:00:49', '1', '9', '5', '黑龙江私营工厂寻找货运物流', '2', '已修改 or_size 。'), ('30', '2014-08-27 14:01:00', '1', '9', '4', '黑龙江私营工厂寻找货运物流', '2', '已修改 or_size 。'), ('31', '2014-08-27 14:01:04', '1', '9', '3', '黑龙江私营工厂寻找货运物流', '2', '已修改 or_size 。'), ('32', '2014-08-27 14:01:10', '1', '9', '2', '黑龙江私营工厂寻找货运物流', '2', '已修改 or_size 。'), ('33', '2014-08-27 14:01:16', '1', '9', '1', '黑龙江私营工厂寻找货运物流', '2', '已修改 or_size 。'), ('34', '2014-09-02 13:53:54', '1', '7', '8', '夜雨闻铃', '3', ''), ('35', '2014-09-02 13:53:54', '1', '7', '7', '111111', '3', ''), ('36', '2014-09-02 15:16:47', '1', '7', '9', '夜雨闻铃', '3', ''), ('37', '2014-09-02 15:20:36', '1', '7', '10', '夜雨闻铃', '3', ''), ('38', '2014-09-02 15:53:42', '1', '7', '3', '11', '3', ''), ('39', '2014-09-04 17:33:36', '1', '12', '1', '挂车', '1', ''), ('40', '2014-09-04 17:33:43', '1', '12', '2', '平板车', '1', ''), ('41', '2014-09-04 17:33:58', '1', '12', '3', '厢式车', '1', ''), ('42', '2014-09-07 13:21:29', '1', '9', '5', '黑龙江私营工厂寻找货运物流1', '2', '已修改 or_title 。'), ('43', '2014-09-07 13:21:36', '1', '9', '4', '黑龙江私营工厂寻找货运物流2', '2', '已修改 or_title 。'), ('44', '2014-09-07 13:21:46', '1', '9', '3', '黑龙江私营工厂寻找货运物流3', '2', '已修改 or_title 。'), ('45', '2014-09-07 13:21:53', '1', '9', '2', '黑龙江私营工厂寻找货运物流4', '2', '已修改 or_title 。'), ('46', '2014-09-07 13:21:59', '1', '9', '1', '黑龙江私营工厂寻找货运物流5', '2', '已修改 or_title 。');
COMMIT;

-- ----------------------------
--  Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `django_content_type`
-- ----------------------------
BEGIN;
INSERT INTO `django_content_type` VALUES ('1', 'log entry', 'admin', 'logentry'), ('2', 'permission', 'auth', 'permission'), ('3', 'group', 'auth', 'group'), ('4', 'user', 'auth', 'user'), ('5', 'content type', 'contenttypes', 'contenttype'), ('6', 'session', 'sessions', 'session'), ('7', '发货企业', 'transport', 'client'), ('8', '货车司机', 'transport', 'driver'), ('9', '订单', 'transport', 'order'), ('10', '订单报价', 'transport', 'offer'), ('11', '位置信息', 'transport', 'location'), ('12', '货车类型管理', 'transport', 'truck'), ('13', '司机在线位置', 'transport', 'online'), ('14', '推送记录', 'transport', 'push');
COMMIT;

-- ----------------------------
--  Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `django_session`
-- ----------------------------
BEGIN;
INSERT INTO `django_session` VALUES ('oxic58ftltngepqns4pcz88pxmyxs6hk', 'M2Q3N2YzMzI4Mjg5YmVkYTFhZGE4YWJlODJmODhhMWU5ZmEwNzI1MDp7InVzZXJuYW1lIjoiMTEifQ==', '2014-09-06 12:29:59'), ('t70yr1x4w3bdvxsgvay9cfbqy79eqyxb', 'M2UzOGU0NjZjMDg0ZjUwNWQ1MTBlYWNmNzEwZTdlNjU3N2M1OTY3Njp7InVzZXJuYW1lIjoiXHU0ZTFiXHU4ZmRjXHU0ZTFjIiwidXNlcl9pZCI6MTEsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-09-21 05:54:34'), ('de6f1ehahtiauyllqn7rq5rpe3dyc5g8', 'MmNjNzRlYzNiMzcyYTBjMzVhODgxZGE0OTBkYjllYWQ2MTU3N2JiMjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-08-30 07:10:36'), ('6n9cj8ekpe7gfnwzca4nj5oc4y2a4zik', 'NTA0YjlmMjg2MzQ0MWM1MGE1MDVjNTU0YzY3Y2YxYmQzN2M5ZjY3Njp7InVzZXJuYW1lIjoiXHU0ZTFiXHU4ZmRjXHU0ZTFjIiwidXNlcl9pZCI6MiwiX2F1dGhfdXNlcl9pZCI6MSwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2014-09-17 11:41:46'), ('4iby6bv7x3ou7dv2i5dphnk8mbybzd1l', 'NTA0YjlmMjg2MzQ0MWM1MGE1MDVjNTU0YzY3Y2YxYmQzN2M5ZjY3Njp7InVzZXJuYW1lIjoiXHU0ZTFiXHU4ZmRjXHU0ZTFjIiwidXNlcl9pZCI6MiwiX2F1dGhfdXNlcl9pZCI6MSwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQifQ==', '2014-09-11 11:58:49'), ('sooi2inkncgvqq62pifz8sqm9xq33jc4', 'ZWU3M2RiYmJhOWIxNzVjZDg3MGE4M2NmODcyOTcwN2I5MDUzNDI4Njp7InVzZXJuYW1lIjoiXHU0ZTFiXHU4ZmRjXHU0ZTFjIiwidXNlcl9pZCI6MiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoxfQ==', '2014-09-09 06:48:55'), ('txkpo21v9ztpxuaz9wz81bilc7ny9ks3', 'M2Y3MjUyZTZmYWNkZjUwYTllMDhmMzE0NzFmMWM3YjY2ZWRjMWJlOTp7InVzZXJuYW1lIjoiXHU0ZTFiXHU4ZmRjXHU0ZTFjIiwidXNlcl9pZCI6Mn0=', '2014-09-16 10:46:03'), ('p87gvplltew7lgjl9srnf6p61dkahn87', 'NzkyMzg0OWFiZmVmMDY1ZDE1Zjg3YmYwYjBkNWZlNTE1YTYwMGZjYzp7fQ==', '2014-09-11 15:00:22'), ('8wvis2abuvr3fnukfcr2dg68sjuq6vna', 'ZWU3M2RiYmJhOWIxNzVjZDg3MGE4M2NmODcyOTcwN2I5MDUzNDI4Njp7InVzZXJuYW1lIjoiXHU0ZTFiXHU4ZmRjXHU0ZTFjIiwidXNlcl9pZCI6MiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2lkIjoxfQ==', '2014-09-14 05:28:36'), ('012ahzbjzzm1nkt7lp08m5ctlr7wvwen', 'MmNjNzRlYzNiMzcyYTBjMzVhODgxZGE0OTBkYjllYWQ2MTU3N2JiMjp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MX0=', '2014-09-16 13:53:34'), ('srrbvgsgyueiyrpbwnb9efgyofxzcqsi', 'M2Y3MjUyZTZmYWNkZjUwYTllMDhmMzE0NzFmMWM3YjY2ZWRjMWJlOTp7InVzZXJuYW1lIjoiXHU0ZTFiXHU4ZmRjXHU0ZTFjIiwidXNlcl9pZCI6Mn0=', '2014-09-23 06:24:39');
COMMIT;

-- ----------------------------
--  Table structure for `transport_client`
-- ----------------------------
DROP TABLE IF EXISTS `transport_client`;
CREATE TABLE `transport_client` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `clt_mail` varchar(75) NOT NULL,
  `clt_pwd` varchar(20) NOT NULL,
  `clt_name` varchar(50) NOT NULL,
  `clt_tel` varchar(30) NOT NULL,
  `clt_company` varchar(50) NOT NULL,
  `clt_position` varchar(30) NOT NULL,
  `clt_industry` varchar(30) NOT NULL,
  `clt_from` varchar(30) NOT NULL,
  `clt_conf_mail` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `transport_client`
-- ----------------------------
BEGIN;
INSERT INTO `transport_client` VALUES ('4', 'test@sina.com', '111111', '11', '13945181460', '1', '未选择', '未选择', '未选择', '0'), ('2', 'congyuandong@sina.com', '111111', '丛远东', '13136652522', '哈尔滨工程大学', '首席执行官', '化学品和塑料工业', '选择风格', '1'), ('5', 'congyuandong@163.com', '111111', '丛远东', '13945181460', '哈工程', '未选择', '未选择', '未选择', '0'), ('6', 'test@163.com', '111111', '丛远东', '13945181460', '哈工程', '所有者', '农业', '未选择', '0'), ('11', '303331934@qq.com', '123456', '丛远东', '13945181460', '哈工程', '董事/总经理', '快速消费品', '百度搜索引擎', '1');
COMMIT;

-- ----------------------------
--  Table structure for `transport_driver`
-- ----------------------------
DROP TABLE IF EXISTS `transport_driver`;
CREATE TABLE `transport_driver` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dr_name` varchar(50) NOT NULL,
  `dr_iden` varchar(50) NOT NULL,
  `dr_tel` varchar(30) NOT NULL,
  `dr_number` varchar(50) NOT NULL,
  `dr_hand` varchar(50) NOT NULL,
  `dr_type` varchar(50) NOT NULL,
  `dr_length` varchar(50) NOT NULL,
  `dr_weight` varchar(50) NOT NULL,
  `dr_pwd` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `transport_driver`
-- ----------------------------
BEGIN;
INSERT INTO `transport_driver` VALUES ('1', '丛远东3', '4', '13136652521', '苏F123', '敌法', '拖车', '100', '100', '1234'), ('2', '丛远东2', '320623199007316992', '1', '黑A 123456', '黑A 123456', '拖车', '12', '12', 'qwer4321'), ('8', '刘启超', '3206199007316992', '2', '黑A12345', 'EGAFA', '火车', '12', '12', '123'), ('7', '丛远东1', '123', '123', '123', '123', '拖车', '12米', '12吨', '123'), ('9', '22', '22', '22', '77', '77', 'edu.hrbeu.ice.util.Type@4297c600', '77', '77', '22');
COMMIT;

-- ----------------------------
--  Table structure for `transport_location`
-- ----------------------------
DROP TABLE IF EXISTS `transport_location`;
CREATE TABLE `transport_location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lo_order_id` int(11) NOT NULL,
  `lo_driver_id` int(11) NOT NULL,
  `lo_longitude` decimal(15,8) NOT NULL,
  `lo_latitude` decimal(15,8) NOT NULL,
  `lo_location` varchar(500) NOT NULL,
  `lo_update` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `transport_location_96faca15` (`lo_order_id`),
  KEY `transport_location_419dc95a` (`lo_driver_id`)
) ENGINE=MyISAM AUTO_INCREMENT=98 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `transport_location`
-- ----------------------------
BEGIN;
INSERT INTO `transport_location` VALUES ('1', '1', '7', '126.68988000', '45.78097000', '黑龙江省哈尔滨市南岗区文庙街', '2014-08-26 16:00:00'), ('2', '1', '7', '126.68989000', '45.78099400', '黑龙江省哈尔滨市南岗区文庙街', '2014-08-27 04:00:00'), ('3', '1', '7', '126.68988000', '45.78098000', '黑龙江省哈尔滨市南岗区文庙街', '2014-08-27 11:37:23'), ('4', '1', '7', '126.68975000', '45.78074000', '黑龙江省哈尔滨市南岗区文庙街', '2014-08-27 11:44:15'), ('5', '2', '8', '126.68992000', '45.78112000', '黑龙江省哈尔滨市南岗区文庙街', '2014-08-27 12:03:17'), ('6', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:25:53'), ('7', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:25:54'), ('8', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:25:56'), ('9', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:25:58'), ('10', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:00'), ('11', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:02'), ('12', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:04'), ('13', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:06'), ('14', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:08'), ('15', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:10'), ('16', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:12'), ('17', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:14'), ('18', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:17'), ('19', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:19'), ('20', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:21'), ('21', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:22'), ('22', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:24'), ('23', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:26'), ('24', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:28'), ('25', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:30'), ('26', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:32'), ('27', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:34'), ('28', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:36'), ('29', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:38'), ('30', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:40'), ('31', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:42'), ('32', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:44'), ('33', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:47'), ('34', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:48'), ('35', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:50'), ('36', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:52'), ('37', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:54'), ('38', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:56'), ('39', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:26:58'), ('40', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:00'), ('41', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:02'), ('42', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:04'), ('43', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:06'), ('44', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:08'), ('45', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:10'), ('46', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:12'), ('47', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:14'), ('48', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:16'), ('49', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:19'), ('50', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:20'), ('51', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:22'), ('52', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:24'), ('53', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:26'), ('54', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:28'), ('55', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:31'), ('56', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:52'), ('57', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:54'), ('58', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:56'), ('59', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:27:58'), ('60', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:00'), ('61', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:02'), ('62', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:04'), ('63', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:06'), ('64', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:08'), ('65', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:11'), ('66', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:12'), ('67', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:14'), ('68', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:17'), ('69', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:18'), ('70', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:20'), ('71', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:22'), ('72', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:24'), ('73', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:26'), ('74', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:28'), ('75', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:30'), ('76', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:33'), ('77', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:34'), ('78', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:36'), ('79', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:38'), ('80', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:40'), ('81', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:42'), ('82', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:44'), ('83', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:46'), ('84', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:48'), ('85', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:50'), ('86', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:52'), ('87', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:55'), ('88', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:56'), ('89', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:28:58'), ('90', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:29:00'), ('91', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:29:02'), ('92', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:29:04'), ('93', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:29:06'), ('94', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:29:08'), ('95', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:29:10'), ('96', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:29:12'), ('97', '1', '8', '126.68987000', '45.78101300', '黑龙江省哈尔滨市南岗区文庙街', '2014-09-09 06:29:14');
COMMIT;

-- ----------------------------
--  Table structure for `transport_offer`
-- ----------------------------
DROP TABLE IF EXISTS `transport_offer`;
CREATE TABLE `transport_offer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `of_order_id` int(11) NOT NULL,
  `of_driver_id` int(11) NOT NULL,
  `of_price` decimal(15,5) NOT NULL,
  `of_distance` decimal(15,5) NOT NULL,
  `of_update` datetime NOT NULL,
  `of_confirm` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `transport_offer_e789bb06` (`of_order_id`),
  KEY `transport_offer_278bb2e3` (`of_driver_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `transport_offer`
-- ----------------------------
BEGIN;
INSERT INTO `transport_offer` VALUES ('1', '1', '1', '150.00000', '211.00000', '2014-08-20 15:52:52', '0'), ('2', '1', '8', '55.00000', '22.00000', '2014-08-11 15:52:57', '1'), ('11', '5', '8', '855.00000', '0.00000', '2014-09-09 06:23:04', '0'), ('4', '3', '7', '6333.00000', '11.00000', '2014-08-15 15:53:06', '1'), ('12', '7', '8', '552.00000', '0.00000', '2014-09-09 06:23:13', '0'), ('8', '1', '7', '666.00000', '12.00000', '2014-09-09 06:20:37', '0'), ('9', '5', '7', '99.00000', '0.00000', '2014-08-27 11:56:48', '0'), ('10', '7', '7', '555.00000', '0.00000', '2014-09-09 06:20:17', '1');
COMMIT;

-- ----------------------------
--  Table structure for `transport_online`
-- ----------------------------
DROP TABLE IF EXISTS `transport_online`;
CREATE TABLE `transport_online` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `on_driver_id` int(11) NOT NULL,
  `on_longitude` decimal(15,8) NOT NULL,
  `on_latitude` decimal(15,8) NOT NULL,
  `on_update` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `transport_online_fa934b79` (`on_driver_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `transport_online`
-- ----------------------------
BEGIN;
INSERT INTO `transport_online` VALUES ('1', '8', '126.68985748', '45.78097153', '2014-09-09 19:00:00'), ('2', '7', '126.68987274', '45.78100586', '2014-09-09 18:21:48');
COMMIT;

-- ----------------------------
--  Table structure for `transport_order`
-- ----------------------------
DROP TABLE IF EXISTS `transport_order`;
CREATE TABLE `transport_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `or_client_id` int(11) NOT NULL,
  `or_id` varchar(50) NOT NULL,
  `or_update` datetime NOT NULL,
  `or_start` varchar(500) NOT NULL,
  `or_end` varchar(500) NOT NULL,
  `or_push` int(11) NOT NULL,
  `or_pushTime` datetime NOT NULL,
  `or_startTime` datetime NOT NULL,
  `or_endTime` datetime NOT NULL,
  `or_title` varchar(200) NOT NULL,
  `or_name` varchar(200) NOT NULL,
  `or_price` decimal(15,5) NOT NULL,
  `or_board` int(11) NOT NULL,
  `or_number` int(11) NOT NULL,
  `or_weight` decimal(15,5) NOT NULL,
  `or_size_l` decimal(15,5) NOT NULL,
  `or_size_w` decimal(15,5) NOT NULL,
  `or_size_h` decimal(15,5) NOT NULL,
  `or_volume` decimal(15,5) NOT NULL,
  `or_truck` varchar(50) NOT NULL,
  `or_length` decimal(15,5) NOT NULL,
  `or_isDanger` varchar(50) NOT NULL,
  `or_isHeap` varchar(50) NOT NULL,
  `or_isHand` varchar(50) NOT NULL,
  `or_isAssist` varchar(50) NOT NULL,
  `or_isInsurance` varchar(50) NOT NULL,
  `or_request` varchar(500) DEFAULT NULL,
  `or_status` int(11) NOT NULL,
  `or_longitude` decimal(15,8) NOT NULL,
  `or_latitude` decimal(15,8) NOT NULL,
  `or_view` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `or_id` (`or_id`),
  KEY `transport_order_00d498b4` (`or_client_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `transport_order`
-- ----------------------------
BEGIN;
INSERT INTO `transport_order` VALUES ('1', '2', '2014082401', '2014-08-24 15:48:23', '哈尔滨工程大学', '南京理工大学', '5', '2014-09-03 15:17:58', '2014-08-24 06:34:22', '2014-08-24 06:34:24', '黑龙江私营工厂寻找货运物流5', '至诚迅达', '12.00000', '12', '1212', '12.00000', '0.00000', '0.00000', '0.00000', '12.00000', '12', '12.00000', '1', '1', '1', '1', '1', '这是说明', '1', '126.69562600', '45.78603400', '57'), ('2', '2', '2014082402', '2014-08-24 15:48:25', '哈尔滨工程大学', '南京理工大学', '5', '2014-09-09 15:18:04', '2014-08-24 06:34:22', '2014-08-24 06:34:24', '黑龙江私营工厂寻找货运物流4', '至诚迅达', '12.00000', '12', '1212', '12.00000', '0.00000', '0.00000', '0.00000', '12.00000', '12', '12.00000', '1', '1', '1', '1', '1', '这是说明', '0', '126.68549300', '45.77155200', '4'), ('3', '2', '2014082403', '2014-08-24 15:48:25', '哈尔滨工程大学', '南京理工大学', '5', '2014-09-09 15:18:09', '2014-08-24 06:34:22', '2014-08-24 06:34:24', '黑龙江私营工厂寻找货运物流3', '至诚迅达', '12.00000', '12', '1212', '12.00000', '0.00000', '0.00000', '0.00000', '12.00000', '12', '12.00000', '1', '1', '1', '1', '1', '这是说明', '1', '126.68549300', '45.77155200', '5'), ('4', '2', '2014082405', '2014-08-24 15:48:25', '哈尔滨工程大学', '南京理工大学', '5', '2014-09-09 15:18:12', '2014-08-24 06:34:22', '2014-08-24 06:34:24', '黑龙江私营工厂寻找货运物流2', '至诚迅达', '12.00000', '12', '1212', '12.00000', '0.00000', '0.00000', '0.00000', '12.00000', '12', '12.00000', '1', '1', '1', '1', '1', '这是说明', '0', '126.68067800', '45.78648700', '9'), ('5', '2', '2014082406', '2014-08-24 15:48:25', '哈尔滨工程大学', '南京理工大学', '5', '2014-09-09 15:18:14', '2014-08-24 06:34:22', '2014-08-24 06:34:24', '黑龙江私营工厂寻找货运物流1', '至诚迅达', '12.00000', '12', '1212', '12.00000', '0.00000', '0.00000', '0.00000', '12.00000', '12', '12.00000', '1', '1', '1', '1', '1', '这是说明', '0', '126.68649900', '45.78492800', '25'), ('6', '2', '140905100000', '2014-09-05 13:09:16', '黑龙江省哈尔滨市南岗区松鹤路', '长白山风景区', '5', '2014-09-09 15:18:16', '2014-09-05 10:00:00', '2014-09-19 12:00:00', '工程大学15公寓需车', '石猴', '150000.00000', '4', '1', '5000.00000', '3.00000', '4.00000', '3.00000', '15.00000', '挂车', '12.00000', '否', '否', '否', '无', '否', '没有说明', '0', '126.68614800', '45.77712100', '0'), ('7', '2', '140905100001', '2014-09-05 13:14:09', '黑龙江省哈尔滨市南岗区松鹤路', '长白山风景区', '5', '2014-09-09 15:18:19', '2014-09-05 10:00:00', '2014-09-19 12:00:00', '工程大学15公寓需车', '石猴', '150000.00000', '4', '1', '5000.00000', '3.00000', '4.00000', '3.00000', '15.00000', '挂车', '12.00000', '否', '否', '否', '无', '否', '没有说明', '1', '126.68614800', '45.77712100', '6'), ('8', '2', '140909100000', '2014-09-09 17:25:26', '黑龙江省哈尔滨市道外区一机路', '哈工程', '10', '2014-09-09 17:25:26', '2014-09-09 19:00:00', '2014-09-25 17:24:00', '测试推送半径1', '测试', '1.00000', '1', '1', '1.00000', '1.00000', '1.00000', '1.00000', '1.00000', '挂车', '12.00000', '否', '否', '否', '装卸都需要', '否', '没有说明', '0', '126.71348400', '45.78730400', '0');
COMMIT;

-- ----------------------------
--  Table structure for `transport_push`
-- ----------------------------
DROP TABLE IF EXISTS `transport_push`;
CREATE TABLE `transport_push` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pu_order_id` int(11) NOT NULL,
  `pu_driver_id` int(11) NOT NULL,
  `pu_count` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `transport_push_c1801def` (`pu_order_id`),
  KEY `transport_push_4f9a26f2` (`pu_driver_id`)
) ENGINE=MyISAM AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `transport_push`
-- ----------------------------
BEGIN;
INSERT INTO `transport_push` VALUES ('28', '2', '8', '1'), ('29', '3', '8', '1'), ('30', '4', '8', '1'), ('31', '5', '8', '1'), ('32', '6', '8', '1'), ('33', '7', '8', '1'), ('34', '2', '7', '1'), ('35', '3', '7', '1'), ('36', '4', '7', '1'), ('37', '5', '7', '1'), ('38', '6', '7', '1'), ('39', '7', '7', '1');
COMMIT;

-- ----------------------------
--  Table structure for `transport_truck`
-- ----------------------------
DROP TABLE IF EXISTS `transport_truck`;
CREATE TABLE `transport_truck` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tr_type` varchar(100) NOT NULL,
  `tr_sort` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
--  Records of `transport_truck`
-- ----------------------------
BEGIN;
INSERT INTO `transport_truck` VALUES ('1', '挂车', '0'), ('2', '平板车', '1'), ('3', '厢式车', '2');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
