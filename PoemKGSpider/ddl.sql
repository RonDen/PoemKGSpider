use poemkg2;

show tables;


select * from poemkg2.poem where poem.topic <> "";
truncate poemkg2.poem;

select count(*) from poemkg2.author;
select * from poemkg2.author;
truncate poemkg2.author;


CREATE TABLE `poemkg2`.`poem`  (
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
  `topic` varchar(100) NOT NULL DEFAULT "" COMMENT  '所在topic',
  `book` varchar(100) NOT NULL DEFAULT "" COMMENT  '来源书籍',
  PRIMARY KEY (`id`),
  INDEX `origin_id_idx`(`origin_id`) USING BTREE,
  INDEX `title_idx`(`title`) USING BTREE,
  INDEX `author_idx`(`author`) USING BTREE,
  INDEX `dynasty`(`dynasty`) USING BTREE,
  INDEX `book_idx`(`book`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;


CREATE TABLE `poemkg2`.`author`  (
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


select * from poemkg2.topic;
drop table poemkg2.topic;
truncate table poemkg2.topic;

CREATE TABLE `poemkg2`.`topic` (
    `id` int NOT NULL AUTO_INCREMENT COMMENT 'mysql自增id',
    `origin` varchar(20) NOT NULL DEFAULT "" COMMENT '爬取来源',
    `origin_id` int NOT NULL DEFAULT -1 COMMENT '在爬取来源中的id',
    `name` varchar(30) NOT NULL DEFAULT "" COMMENT '主题名称',
    `url` varchar(200) NOT NULL DEFAULT "" COMMENT '该主题在来源中的url',
    `create_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录创建时间，用于记录和更新',
    `update_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录修改时间',
    PRIMARY KEY (`id`),
    INDEX `origin_id_idx`(`origin_id`) USING BTREE,
    INDEX `name_idx`(`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;

select * from `poemkg2`.`book`;
drop table `poemkg2`.`book`;
truncate table `poemkg2`.`book`;

CREATE TABLE `poemkg2`.`book` (
    `id` int NOT NULL AUTO_INCREMENT COMMENT 'mysql自增id',
    `origin` varchar(20) NOT NULL DEFAULT "" COMMENT '爬取来源',
    `origin_id` int NOT NULL DEFAULT -1 COMMENT '在爬取来源中的id',
    `url` varchar(200) NOT NULL DEFAULT "" COMMENT '该古籍在来源中的url',
    `title` varchar(30) NOT NULL DEFAULT "" COMMENT '书籍名称',
    `author` varchar(30) NOT NULL DEFAULT "" COMMENT '作者名称',
    `author_id` int NOT NULL DEFAULT 0 COMMENT '作者在原站中的id',
    `detail` longtext not null COMMENT '古籍的描述信息',
    `img_url` varchar(200) NOT NULL DEFAULT "" COMMENT '古籍的图片信息',
    `chapter` varchar(255) NOT NULL DEFAULT "" COMMENT '古籍篇章信息',
    `create_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录创建时间，用于记录和更新',
    `update_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录修改时间',
    PRIMARY KEY (`id`),
    INDEX `origin_id_idx`(`origin_id`) USING BTREE,
    INDEX `author_name_idx`(`author`) USING BTREE,
    INDEX `author_id_idx`(`author_id`) USING BTREE,
    INDEX `title_idx`(`title`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;

select * from `poemkg2`.`dynasty`;
drop table `poemkg2`.`dynasty`;
truncate table `poemkg2`.`dynasty`;

CREATE TABLE `poemkg2`.`dynasty` (
    `id` int NOT NULL AUTO_INCREMENT COMMENT 'mysql自增id',
    `origin` varchar(20) NOT NULL DEFAULT "" COMMENT '爬取来源',
    `origin_id` int NOT NULL DEFAULT -1 COMMENT '在爬取来源中的id',
    `url` varchar(200) NOT NULL DEFAULT "" COMMENT '该朝代描述在来源中的url',
    `name` varchar(10) NOT NULL DEFAULT "" COMMENT '朝代名称',
    `start` int not null default 0 comment '朝代开始年份',
    `end` int not null default 0 comment '朝代结束年份',
    `detail` longtext not null COMMENT '该朝代的详细描述信息',
    `create_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录创建时间，用于记录和更新',
    `update_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录修改时间',
    PRIMARY KEY (`id`),
    INDEX `origin_id_idx`(`origin_id`) USING BTREE,
    INDEX `start_idx`(`start`) USING BTREE,
    INDEX `end_idx`(`end`) USING BTREE,
    INDEX `name_idx`(`name`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;

select * from `poemkg2`.`idiom`;
drop table `poemkg2`.`idiom`;
truncate table `poemkg2`.`idiom`;

CREATE TABLE `poemkg2`.`idiom` (
    `id` int NOT NULL AUTO_INCREMENT COMMENT 'mysql自增id',
    `origin` varchar(20) NOT NULL DEFAULT "" COMMENT '爬取来源',
    `origin_id` int NOT NULL DEFAULT -1 COMMENT '在爬取来源中的id',
    `url` varchar(200) NOT NULL DEFAULT "" COMMENT '该成语的url',
    `content` varchar(30) NOT NULL DEFAULT "" COMMENT '成语内容',
    `pingyin` varchar(150) NOT NULL DEFAULT "" COMMENT '成语拼音',
    `explain` varchar(255) NOT NULL DEFAULT "" COMMENT '成语解释',
    `come_from` varchar(255) NOT NULL DEFAULT "" COMMENT '成语出处',
    `example` varchar(255) NOT NULL DEFAULT "" COMMENT '成语例句',
    `create_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录创建时间，用于记录和更新',
    `update_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录修改时间',
    PRIMARY KEY (`id`),
    INDEX `origin_id_idx`(`origin_id`) USING BTREE,
    INDEX `content_idx`(`content`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;

select * from `poemkg2`.`mingjv`;
drop table `poemkg2`.`mingjv`;
truncate table `poemkg2`.`mingjv`;

CREATE TABLE `poemkg2`.`mingjv` (
    `id` int NOT NULL AUTO_INCREMENT COMMENT 'mysql自增id',
    `origin` varchar(20) NOT NULL DEFAULT "" COMMENT '爬取来源',
    `origin_id` int NOT NULL DEFAULT -1 COMMENT '在爬取来源中的id',
    `url` varchar(200) NOT NULL DEFAULT "" COMMENT '该成语的url',
    `content` varchar(50) NOT NULL DEFAULT "" COMMENT '名句内容',
    `come_from` varchar(50) NOT NULL DEFAULT "" COMMENT '名句出处',
    `come_from_id` int NOT NULL DEFAULT -1 COMMENT '名句出处的id',
    `author` varchar(20) NOT NULL DEFAULT "" COMMENT '名句作者',
    `author_id` int NOT NULL DEFAULT -1 COMMENT '名句作者的id',
    `create_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录创建时间，用于记录和更新',
    `update_at` DATETIME NOT NULL DEFAULT NOW() COMMENT '该条记录修改时间',
    PRIMARY KEY (`id`),
    INDEX `origin_id_idx`(`origin_id`) USING BTREE,
    INDEX `content_idx`(`content`) USING BTREE,
    INDEX `author_idx`(`author`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 AUTO_INCREMENT=1;
