CREATE TABLE `birthday_friends` (
 `id` int(6) NOT NULL AUTO_INCREMENT,
 `user_id` int(20) NOT NULL,
 `name` varchar(40) COLLATE utf8mb4_unicode_ci NOT NULL,
 `date` date NOT NULL,
 PRIMARY KEY (`id`)
) 