CREATE TABLE `poemkg`.`poem`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'mysql自增id',
  `origin` varchar(20) NOT NULL DEFAULT "" COMMENT '爬取来源',
  `origin_id` int NOT NULL DEFAULT -1 COMMENT '在爬取来源中的id',
  `url` varchar(200) NOT NULL DEFAULT "" COMMENT '诗词来源的url',
  `title` varchar(200) NOT NULL DEFAULT "" COMMENT '诗词标题',
  `content` longtext NOT NULL COMMENT '诗词内容',
  `pingyin` longtext NOT NULL COMMENT '诗词的拼音',
  `author_id` int NOT NULL DEFAULT -1 COMMENT '诗词作者，来源网站中的作者id，-1表示没有更多信息',
  `author` varchar(20) NOT NULL DEFAULT "" COMMENT '作者姓名',
  `author_url` varchar(200) NULL DEFAULT "" COMMENT 'url，如果author_id为-1，url无效',
  `dynasty` varchar(10) NOT NULL DEFAULT "" COMMENT '诗歌创作朝代',
  `translate` longtext NOT NULL COMMENT '诗歌的翻译信息',
  `shangxi` varchar(200) NOT NULL DEFAULT "" COMMENT '诗歌的赏析信息，使用逗号分隔赏析文章列表',
  `create_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录创建时间，用于记录和更新',
  `update_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录修改时间',
  PRIMARY KEY (`id`),
  INDEX `origin_id_idx`(`origin_id`) USING BTREE,
  INDEX `title_idx`(`title`) USING BTREE,
  INDEX `author_idx`(`author`) USING BTREE,
  INDEX `dynasty`(`dynasty`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;


CREATE TABLE `poemkg`.`author`  (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'mysql自增id',
  `origin` varchar(20) NOT NULL DEFAULT "" COMMENT '爬取来源',
  `origin_id` int NOT NULL DEFAULT -1 COMMENT '在爬取来源中的id',
  `url` varchar(200) NOT NULL DEFAULT "" COMMENT '该作者在来源中的url',
  `name` varchar(30) NOT NULL DEFAULT "" COMMENT '作者名称',
  `detail` longtext NOT NULL COMMENT '作者详细信息',
  `dynasty` varchar(10) NOT NULL DEFAULT "" COMMENT '诗歌创作朝代',
  `img_url` varchar(200) NOT NULL DEFAULT "" COMMENT '作者照片或图像url',
  `create_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录创建时间，用于记录和更新',
  `update_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录修改时间',
  PRIMARY KEY (`id`),
  INDEX `origin_id_idx`(`origin_id`) USING BTREE,
  INDEX `name_idx`(`name`) USING BTREE,
  INDEX `dynasty`(`dynasty`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;
