-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 12, 2021 at 06:55 AM
-- Server version: 5.7.32
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scheduling`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add department', 7, 'add_department'),
(26, 'Can change department', 7, 'change_department'),
(27, 'Can delete department', 7, 'delete_department'),
(28, 'Can view department', 7, 'view_department'),
(29, 'Can add instructor', 8, 'add_instructor'),
(30, 'Can change instructor', 8, 'change_instructor'),
(31, 'Can delete instructor', 8, 'delete_instructor'),
(32, 'Can view instructor', 8, 'view_instructor'),
(33, 'Can add meeting time', 9, 'add_meetingtime'),
(34, 'Can change meeting time', 9, 'change_meetingtime'),
(35, 'Can delete meeting time', 9, 'delete_meetingtime'),
(36, 'Can view meeting time', 9, 'view_meetingtime'),
(37, 'Can add room', 10, 'add_room'),
(38, 'Can change room', 10, 'change_room'),
(39, 'Can delete room', 10, 'delete_room'),
(40, 'Can view room', 10, 'view_room'),
(41, 'Can add course', 11, 'add_course'),
(42, 'Can change course', 11, 'change_course'),
(43, 'Can delete course', 11, 'delete_course'),
(44, 'Can view course', 11, 'view_course');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$260000$o9nCvhYTc2n7lHxJ8z5iMa$+5cYfeootjLbbggeA6GdqdytkQNoVpAQr6Fqa4tAbyk=', '2021-06-02 01:56:49.809245', 1, 'admin', '', '', 'admin@gmail.com', 1, 1, '2021-06-02 01:56:26.510023');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-06-02 01:58:51.902919', '2', 'Stat', 1, '[{\"added\": {}}]', 11, 1),
(2, '2021-06-02 02:07:41.709696', '2', 'Loknath Regmi', 1, '[{\"added\": {}}]', 8, 1),
(3, '2021-06-02 02:07:48.376053', '3', 'IT', 1, '[{\"added\": {}}]', 11, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(11, 'scheduling_app', 'course'),
(7, 'scheduling_app', 'department'),
(8, 'scheduling_app', 'instructor'),
(9, 'scheduling_app', 'meetingtime'),
(10, 'scheduling_app', 'room'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-06-01 15:34:01.157938'),
(2, 'auth', '0001_initial', '2021-06-01 15:34:01.851720'),
(3, 'admin', '0001_initial', '2021-06-01 15:34:02.003333'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-06-01 15:34:02.029507'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-06-01 15:34:02.051165'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-06-01 15:34:02.158206'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-06-01 15:34:02.228202'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-06-01 15:34:02.303890'),
(9, 'auth', '0004_alter_user_username_opts', '2021-06-01 15:34:02.326719'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-06-01 15:34:02.405100'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-06-01 15:34:02.411559'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-06-01 15:34:02.435425'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-06-01 15:34:02.518111'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-06-01 15:34:02.597623'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-06-01 15:34:02.669994'),
(16, 'auth', '0011_update_proxy_permissions', '2021-06-01 15:34:02.695034'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-06-01 15:34:02.772312'),
(18, 'scheduling_app', '0001_initial', '2021-06-01 15:34:03.040093'),
(19, 'sessions', '0001_initial', '2021-06-01 15:34:03.101220');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('nf3yuibydmdkkk5bsreono29t9hk0ihk', '.eJxVjDsOwyAQBe9CHSFg-Tllep8BLbAEJxGWjF1FuXtsyUXSvpl5bxZwW2vYOi1hyuzKJLv8bhHTk9oB8gPbfeZpbusyRX4o_KSdj3Om1-10_w4q9rrXJiYPRaNSAEkIAk2o3ZAV2YhFJAHGFud0cr4ojARo1W4ZqbKWA3r2-QLkZDe8:1loG7l:bkpNPopZYPKj2WKLd59ytK1XvofbGaOI2WIEsH0OXUQ', '2021-06-16 01:56:49.818864');

-- --------------------------------------------------------

--
-- Table structure for table `scheduling_app_course`
--

CREATE TABLE `scheduling_app_course` (
  `id` bigint(20) NOT NULL,
  `number` varchar(200) NOT NULL,
  `sem` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `type` varchar(20) NOT NULL DEFAULT 'TH',
  `maxNoOfStudents` int(11) NOT NULL,
  `periodPerWeek` int(11) NOT NULL,
  `department_id` bigint(20) NOT NULL,
  `instructors_id` bigint(20) NOT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'active'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `scheduling_app_course`
--

INSERT INTO `scheduling_app_course` (`id`, `number`, `sem`, `name`, `type`, `maxNoOfStudents`, `periodPerWeek`, `department_id`, `instructors_id`, `status`) VALUES
(1, 'CSC109', 1, 'Introduction to Information Technology', 'TH', 48, 5, 1, 1, '1'),
(2, 'CSC110', 1, 'C', 'TH', 48, 5, 1, 2, '1'),
(3, 'CSC111', 1, 'Digital Logic', 'TH', 48, 4, 1, 3, '1'),
(4, 'MTH112', 1, 'Mathematics I', 'TH', 48, 6, 1, 4, '1'),
(5, 'PHY113', 1, 'Physics', 'TH', 48, 5, 1, 5, '1'),
(6, 'CSC160', 2, 'Discrete Structure', 'TH', 48, 4, 1, 6, '0'),
(7, 'CSC161', 2, 'Object-Oriented Programming', 'TH', 48, 4, 1, 7, '0'),
(8, 'CSC162', 2, 'Microprocessor', 'TH', 48, 3, 1, 8, '0'),
(9, 'MTH163', 2, 'Mathematics II', 'TH', 48, 5, 1, 4, '0'),
(10, 'STA164', 2, 'Statistics I', 'TH', 48, 5, 1, 9, '0'),
(11, 'CSC206', 3, 'Data Structure and Algorithm', 'TH', 48, 4, 1, 2, '0'),
(12, 'CSC207', 3, 'Numerical Method', 'TH', 48, 3, 1, 3, '0'),
(13, 'CSC208', 3, 'Computer Architecture', 'TH', 48, 3, 1, 1, '0'),
(14, 'CSC209', 3, 'Computer Graphics', 'TH', 48, 4, 1, 10, '0'),
(15, 'STA210', 3, 'Statistics II', 'TH', 48, 5, 1, 11, '0'),
(16, 'CSC257', 4, 'Theory of Computation', 'TH', 48, 4, 1, 12, '0'),
(17, 'CSC258', 4, 'Computer Networks', 'TH', 48, 4, 1, 14, '0'),
(18, 'CSC259', 4, 'Operating Systems', 'TH', 48, 3, 1, 13, '0'),
(19, 'CSC260', 4, 'Database Management System', 'TH', 48, 4, 1, 7, '0'),
(20, 'CSC261', 4, 'Artificial Intelligence', 'TH', 48, 5, 1, 15, '0'),
(21, 'CSC306', 5, 'Compiler', 'TH', 48, 5, 1, 19, '0'),
(22, 'CSC307', 5, 'DAA', 'TH', 48, 5, 1, 16, '0'),
(23, 'CSC38', 5, 'RTOS', 'TH', 48, 5, 1, 24, '0'),
(24, 'CSC110', 1, 'C', 'LAB', 48, 3, 1, 2, '1'),
(25, 'CSC109', 1, 'Introduction to Information Technology', 'LAB', 48, 2, 1, 1, '1'),
(26, 'CSC1110', 1, 'Digital Logic', 'LAB', 48, 2, 1, 3, '1'),
(27, 'Phy113', 1, 'Physics', 'LAB', 48, 2, 1, 5, '1'),
(28, 'CSC160', 2, 'Discrete Structure', 'LAB', 48, 2, 1, 6, '0'),
(29, 'CSC161', 2, 'Subash Manandhar', 'LAB', 48, 3, 1, 7, '0');

-- --------------------------------------------------------

--
-- Table structure for table `scheduling_app_department`
--

CREATE TABLE `scheduling_app_department` (
  `id` bigint(20) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `scheduling_app_department`
--

INSERT INTO `scheduling_app_department` (`id`, `name`) VALUES
(1, 'CSIT'),
(2, 'BCA'),
(3, 'BBA');

-- --------------------------------------------------------

--
-- Table structure for table `scheduling_app_instructor`
--

CREATE TABLE `scheduling_app_instructor` (
  `instructor_id` bigint(20) NOT NULL,
  `id` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `scheduling_app_instructor`
--

INSERT INTO `scheduling_app_instructor` (`instructor_id`, `id`, `name`) VALUES
(1, 'LNR', 'Loknath Regmi'),
(2, 'SBM', 'Satye Bahadur Maharjan'),
(3, 'SD', 'Saroj Dhakal'),
(4, 'MBR', 'Man Bahadur Ranabhat'),
(5, 'DR', 'Dipak Regmi'),
(6, 'DS', 'Deni Shahi'),
(7, 'SM', 'Subash Manandhar'),
(8, 'RRK', 'Roshan Raj Karanjeet'),
(9, 'SR', 'Shishir Regmi'),
(10, 'AD', 'Abhisekh Dewan'),
(11, 'OP', 'Om Prajapati'),
(12, 'TARA', 'Tara Bahadur'),
(13, 'DRG', 'Dadhi Raj Ghimire'),
(14, 'KHK', 'Krishna Hari Karki'),
(15, 'MB', 'Mohan Bhandari'),
(16, 'RT', 'Roshan Tandukar'),
(17, 'AM', 'Aman Maharjan'),
(18, 'NB', 'Nabin Pokharel'),
(19, 'KD', 'Kalyan Dhungel'),
(20, 'NT', 'Nabin Tiwari'),
(21, 'AP', 'Ashok Poudel'),
(22, 'SS', 'Sumanta Silwal'),
(23, 'DW', 'Dipak Wagle'),
(24, 'MK', 'Manjeet Karki'),
(25, 'SG', 'Saroj Ghimire');

-- --------------------------------------------------------

--
-- Table structure for table `scheduling_app_meetingtime`
--

CREATE TABLE `scheduling_app_meetingtime` (
  `meeting_id` bigint(20) NOT NULL,
  `id` varchar(200) NOT NULL,
  `day` varchar(50) NOT NULL,
  `time` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `scheduling_app_meetingtime`
--

INSERT INTO `scheduling_app_meetingtime` (`meeting_id`, `id`, `day`, `time`) VALUES
(1, 'MT1', 'SUN', '11:15 - 12:15'),
(2, 'MT2', 'SUN', '12:15 - 01:15'),
(3, 'MT3', 'SUN', '01:30 - 02:30'),
(4, 'MT4', 'SUN', '03:00 - 04:00'),
(5, 'MT5', 'SUN', '04:00 - 05:00'),
(6, 'MT6', 'MON', '11:15 - 12:15'),
(7, 'MT7', 'MON', '12:15 - 01:15'),
(8, 'MT8', 'MON', '01:30 - 02:30'),
(9, 'MT9', 'MON', '03:00 - 04:00'),
(10, 'MT10', 'MON', '04:00 - 05:00'),
(11, 'MT11', 'TUE', '11:15 - 12:15'),
(12, 'MT12', 'TUE', '12:15 - 01:15'),
(13, 'MT13', 'TUE', '01:30 - 02:30'),
(14, 'MT14', 'TUE', '03:00 - 04:00'),
(15, 'MT15', 'TUE', '04:00 - 05:00'),
(16, 'MT16', 'WED', '11:15 - 12:15'),
(17, 'MT17', 'WED', '12:15 - 01:15'),
(18, 'MT18', 'WED', '01:30 - 02:30'),
(19, 'MT19', 'WED', '03:00 - 04:00'),
(20, 'MT20', 'WED', '04:00 - 05:00'),
(21, 'MT21', 'THU', '11:15 - 12:15'),
(22, 'MT22', 'THU', '12:15 - 01:15'),
(23, 'MT23', 'THU', '01:30 - 02:30'),
(24, 'MT24', 'THU', '03:00 - 04:00'),
(25, 'MT25', 'THU', '04:00 - 05:00'),
(26, 'MT26', 'FRI', '11:15 - 12:15'),
(27, 'MT27', 'FRI', '12:15 - 01:15'),
(28, 'MT28', 'FRI', '01:30 - 02:30'),
(29, 'MT29', 'FRI', '03:00 - 04:00'),
(30, 'MT30', 'FRI', '04:00 - 05:00');

-- --------------------------------------------------------

--
-- Table structure for table `scheduling_app_room`
--

CREATE TABLE `scheduling_app_room` (
  `id` bigint(20) NOT NULL,
  `number` varchar(200) NOT NULL,
  `seatingCapacity` varchar(200) NOT NULL,
  `type` varchar(20) NOT NULL DEFAULT 'TH'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `scheduling_app_room`
--

INSERT INTO `scheduling_app_room` (`id`, `number`, `seatingCapacity`, `type`) VALUES
(1, 'R1', '50', 'TH'),
(2, 'R2', '50', 'TH'),
(3, 'R3', '45', 'TH'),
(4, 'R4', '50', 'TH'),
(5, 'R5', '45', 'TH'),
(6, 'LAB 1', '50', 'LAB'),
(7, 'LAB 2', '48', 'LAB');

-- --------------------------------------------------------

--
-- Table structure for table `scheduling_app_semester`
--

CREATE TABLE `scheduling_app_semester` (
  `id` bigint(20) NOT NULL,
  `sem` int(11) NOT NULL,
  `department_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `scheduling_app_course`
--
ALTER TABLE `scheduling_app_course`
  ADD PRIMARY KEY (`id`),
  ADD KEY `scheduling_app_cours_department_id_0fce4128_fk_schedulin` (`department_id`),
  ADD KEY `scheduling_app_cours_instructors_id_2c34f946_fk_schedulin` (`instructors_id`);

--
-- Indexes for table `scheduling_app_department`
--
ALTER TABLE `scheduling_app_department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scheduling_app_instructor`
--
ALTER TABLE `scheduling_app_instructor`
  ADD PRIMARY KEY (`instructor_id`);

--
-- Indexes for table `scheduling_app_meetingtime`
--
ALTER TABLE `scheduling_app_meetingtime`
  ADD PRIMARY KEY (`meeting_id`);

--
-- Indexes for table `scheduling_app_room`
--
ALTER TABLE `scheduling_app_room`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scheduling_app_semester`
--
ALTER TABLE `scheduling_app_semester`
  ADD PRIMARY KEY (`id`),
  ADD KEY `scheduling_app_semes_department_id_465b175b_fk_schedulin` (`department_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `scheduling_app_department`
--
ALTER TABLE `scheduling_app_department`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `scheduling_app_semester`
--
ALTER TABLE `scheduling_app_semester`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `scheduling_app_semester`
--
ALTER TABLE `scheduling_app_semester`
  ADD CONSTRAINT `scheduling_app_semes_department_id_465b175b_fk_schedulin` FOREIGN KEY (`department_id`) REFERENCES `scheduling_app_department` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
