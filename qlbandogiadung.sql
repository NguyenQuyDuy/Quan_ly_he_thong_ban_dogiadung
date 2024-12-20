-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 04, 2024 at 12:35 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qlbandogiadung`
--

-- --------------------------------------------------------

--
-- Table structure for table `cham_cong`
--

CREATE TABLE `cham_cong` (
  `id` int(11) NOT NULL,
  `ma_nhan_vien` int(11) DEFAULT NULL,
  `ten` varchar(255) NOT NULL,
  `ngay` date DEFAULT NULL,
  `gio_vao` time DEFAULT NULL,
  `gio_ra` time DEFAULT NULL,
  `luong` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cham_cong`
--

INSERT INTO `cham_cong` (`id`, `ma_nhan_vien`, `ten`, `ngay`, `gio_vao`, `gio_ra`, `luong`) VALUES
(6, 8, 'Hoàng Hải Hậu', '2024-06-25', '22:35:53', '22:37:41', 900.00),
(8, 11, 'Nguyễn Nam Trường', '2024-06-26', '06:32:38', '07:03:57', 12520.00),
(9, 8, 'Hoàng Hải Hậu', '2024-06-26', '06:32:38', '07:04:07', 12586.67),
(11, 11, 'Nguyễn Nam Trường', '2024-06-28', '22:59:05', '23:02:07', 1516.67);

-- --------------------------------------------------------

--
-- Table structure for table `don_hang`
--

CREATE TABLE `don_hang` (
  `ma_don_hang` int(11) NOT NULL,
  `ma_san_pham` int(11) DEFAULT NULL,
  `so_luong` int(11) NOT NULL,
  `ngay_dat_hang` date NOT NULL,
  `tong_tien` decimal(10,2) NOT NULL,
  `ma_khach_hang` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `don_hang`
--

INSERT INTO `don_hang` (`ma_don_hang`, `ma_san_pham`, `so_luong`, `ngay_dat_hang`, `tong_tien`, `ma_khach_hang`) VALUES
(32, 2, 10, '2024-06-20', 2000000.00, 1),
(33, 4, 6, '2024-06-20', 720000.00, 1),
(34, 5, 10, '2024-06-20', 1000000.00, 3),
(35, 6, 4, '2024-06-20', 600000.00, 2),
(36, 7, 10, '2024-06-20', 2500000.00, 2),
(37, 6, 4, '2024-06-20', 600000.00, 2),
(38, 6, 4, '2024-06-21', 600000.00, 2),
(39, 7, 2, '2024-06-21', 500000.00, 4),
(40, 5, 10, '2024-06-21', 1000000.00, 2),
(41, 6, 4, '2024-06-21', 600000.00, 4),
(42, 7, 7, '2024-06-22', 1750000.00, 4),
(43, 4, 4, '2024-06-22', 480000.00, 3),
(44, 5, 5, '2024-06-22', 500000.00, 2),
(45, 12, 2, '2024-06-23', 15000000.00, 1),
(47, 11, 5, '2024-06-24', 760000.00, 2),
(48, 14, 2, '2024-06-24', 148000.00, 3),
(49, 11, 5, '2024-06-25', 760000.00, 2),
(50, 13, 5, '2024-06-25', 7500000.00, 4),
(51, 14, 4, '2024-06-25', 296000.00, 2),
(52, 9, 2, '2024-06-26', 400000.00, 3),
(53, 13, 2, '2024-06-28', 3000000.00, 2),
(54, 13, 5, '2024-06-28', 7500000.00, 4),
(55, 13, 2, '2024-06-28', 3000000.00, 2),
(56, 14, 2, '2024-06-28', 148000.00, 4),
(57, 8, 5, '2024-06-28', 500000.00, 2),
(58, 9, 2, '2024-06-28', 400000.00, 2),
(59, 10, 4, '2024-06-28', 300000.00, 3),
(60, 12, 2, '2024-06-28', 15000000.00, 3),
(61, 4, 2, '2024-06-28', 240000.00, 5),
(62, 5, 2, '2024-06-28', 200000.00, 5),
(63, 8, 2, '2024-06-27', 200000.00, 4),
(66, 11, 2, '2024-06-29', 304000.00, 1),
(67, 9, 2, '2024-06-29', 400000.00, 2),
(68, 9, 2, '2024-06-29', 400000.00, 2),
(69, 8, 2, '2024-06-29', 200000.00, 1),
(70, 9, 2, '2024-06-29', 400000.00, 2),
(71, 11, 2, '2024-06-29', 304000.00, 2),
(73, 14, 2, '2024-07-02', 148000.00, 6);

-- --------------------------------------------------------

--
-- Table structure for table `khach_hang`
--

CREATE TABLE `khach_hang` (
  `ma_khach_hang` int(11) NOT NULL,
  `ten_khach_hang` varchar(255) DEFAULT NULL,
  `lien_he_khach_hang` int(11) DEFAULT NULL,
  `dia_chi` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `khach_hang`
--

INSERT INTO `khach_hang` (`ma_khach_hang`, `ten_khach_hang`, `lien_he_khach_hang`, `dia_chi`, `email`) VALUES
(1, 'Bùi Đình Nghệ An', 355554446, 'Nam từ liêm, Hà Nội', 'bdnghe@gmail.com'),
(2, 'Trần Phương Anh', 379824531, 'Cầu giấy, Hà Nội', 'anh@gmail.com'),
(3, 'Nguyễn Văn Nghĩa', 255446665, 'Thôn X, xã Y, huyện Z, Sơn La', 'nghia@gmail.com'),
(4, 'Nguyễn Văn An', 555448888, 'Bắc Từ Liêm Hà Nội', 'a@gmail.com'),
(5, 'Hoàng Trường', 354445559, 'Thôn X, xã Y, huyện Z, Thái Nguyên', 'truong@gmail.com'),
(6, 'Nguyễn Ngọc Ngạn', 355448884, 'Hà Nam', 'ngan@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `quan_li_tai_khoan`
--

CREATE TABLE `quan_li_tai_khoan` (
  `id` int(11) NOT NULL,
  `ten` varchar(255) NOT NULL,
  `mat_khau` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `so_dien_thoai` int(20) DEFAULT NULL,
  `chuc_vu` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `quan_li_tai_khoan`
--

INSERT INTO `quan_li_tai_khoan` (`id`, `ten`, `mat_khau`, `email`, `so_dien_thoai`, `chuc_vu`) VALUES
(1, 'Giàng Xuân Cường', '12345', 'cuong@gmail.com', 123456789, 'admin'),
(8, 'Hoàng Hải Hậu', '12345', 'hau@gmail.com', 125554447, 'stocker'),
(11, 'Nguyễn Nam Trường', '12345', 'truong@gmail.com', 355665554, 'sale'),
(15, 'Nguyễn Nam Can', '12345', 'can@gmail.com', 12345, 'sale'),
(17, 'Phan Lê Vi Thanh', '12345', 'thanh@gmail.com', 355554447, 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `san_pham`
--

CREATE TABLE `san_pham` (
  `ma_san_pham` int(11) NOT NULL,
  `ten_san_pham` varchar(255) NOT NULL,
  `gia` decimal(10,2) NOT NULL,
  `so_luong_ton` int(11) NOT NULL,
  `mo_ta` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `san_pham`
--

INSERT INTO `san_pham` (`ma_san_pham`, `ten_san_pham`, `gia`, `so_luong_ton`, `mo_ta`) VALUES
(2, 'Giấy in văn phòng', 200000.00, 459, 'Giấy in cao cấp'),
(4, 'Bìa đựng hồ sơ', 120000.00, 167, 'Bìa cao cấp'),
(5, 'Bút lông viết bảng', 100000.00, 233, 'Bút lông xịn'),
(6, 'Kẹp giấy', 150000.00, 172, 'Kẹp bướm/kẹp giấy/kẹp tài liệu. ...'),
(7, 'Sổ', 250000.00, 30, 'Sổ, tập tài liệu'),
(8, 'Gôm', 100000.00, 241, 'Gôm, bút tẩy, bút xóa'),
(9, 'Dao dọc giấy', 200000.00, 40, 'dao dọc giấy, băng keo'),
(10, 'Giấy A4 ', 75000.00, 66, 'Giấy A4 Excel 70 gsm'),
(11, 'Máy tính Casio Mx-12B', 152000.00, 16, 'Máy tính xịn, cao cấp'),
(12, 'Băng keo trong f5 100Yard', 7500000.00, 7, 'băng keo trong'),
(13, 'Bìa còng Thiên Long F4', 1500000.00, 796, 'Bìa còng Thiên Long F4 5-7ml'),
(14, 'Kéo văn phòng', 74000.00, 10, 'Kéo văn phòng');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cham_cong`
--
ALTER TABLE `cham_cong`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ma_nhan_vien` (`ma_nhan_vien`);

--
-- Indexes for table `don_hang`
--
ALTER TABLE `don_hang`
  ADD PRIMARY KEY (`ma_don_hang`),
  ADD KEY `ma_khach_hang` (`ma_khach_hang`),
  ADD KEY `ma_san_pham` (`ma_san_pham`);

--
-- Indexes for table `khach_hang`
--
ALTER TABLE `khach_hang`
  ADD PRIMARY KEY (`ma_khach_hang`);

--
-- Indexes for table `quan_li_tai_khoan`
--
ALTER TABLE `quan_li_tai_khoan`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `san_pham`
--
ALTER TABLE `san_pham`
  ADD PRIMARY KEY (`ma_san_pham`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cham_cong`
--
ALTER TABLE `cham_cong`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `don_hang`
--
ALTER TABLE `don_hang`
  MODIFY `ma_don_hang` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=74;

--
-- AUTO_INCREMENT for table `quan_li_tai_khoan`
--
ALTER TABLE `quan_li_tai_khoan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `san_pham`
--
ALTER TABLE `san_pham`
  MODIFY `ma_san_pham` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cham_cong`
--
ALTER TABLE `cham_cong`
  ADD CONSTRAINT `cham_cong_ibfk_1` FOREIGN KEY (`ma_nhan_vien`) REFERENCES `quan_li_tai_khoan` (`id`);

--
-- Constraints for table `don_hang`
--
ALTER TABLE `don_hang`
  ADD CONSTRAINT `don_hang_ibfk_1` FOREIGN KEY (`ma_khach_hang`) REFERENCES `khach_hang` (`ma_khach_hang`),
  ADD CONSTRAINT `don_hang_ibfk_2` FOREIGN KEY (`ma_san_pham`) REFERENCES `san_pham` (`ma_san_pham`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
