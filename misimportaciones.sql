SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS `misimportaciones` ;
CREATE SCHEMA IF NOT EXISTS `misimportaciones` DEFAULT CHARACTER SET utf8 COLLATE utf8_swedish_ci ;
USE `misimportaciones` ;

-- -----------------------------------------------------
-- Table `misimportaciones`.`marcas`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `misimportaciones`.`marcas` (
  `idmarca` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(10) NOT NULL ,
  PRIMARY KEY (`idmarca`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `misimportaciones`.`categorias`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `misimportaciones`.`categorias` (
  `idcategoria` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(10) NOT NULL ,
  PRIMARY KEY (`idcategoria`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `misimportaciones`.`productos`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `misimportaciones`.`productos` (
  `idproducto` INT NOT NULL AUTO_INCREMENT ,
  `idcategoria` INT NOT NULL ,
  `idmarca` INT NOT NULL ,
  `contenido` VARCHAR(6) NULL ,
  `activo` TINYINT(1)  NOT NULL DEFAULT 1 ,
  PRIMARY KEY (`idproducto`) ,
  INDEX `fk_productos_marcas1` (`idmarca` ASC) ,
  INDEX `fk_productos_categorias1` (`idcategoria` ASC) ,
  UNIQUE INDEX `unico` (`idcategoria` ASC, `idmarca` ASC, `contenido` ASC) ,
  CONSTRAINT `fk_productos_marcas1`
    FOREIGN KEY (`idmarca` )
    REFERENCES `misimportaciones`.`marcas` (`idmarca` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_productos_categorias1`
    FOREIGN KEY (`idcategoria` )
    REFERENCES `misimportaciones`.`categorias` (`idcategoria` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `misimportaciones`.`preciosproducto`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `misimportaciones`.`preciosproducto` (
  `idprecioproducto` INT NOT NULL AUTO_INCREMENT ,
  `idproducto` INT NOT NULL ,
  `precio` DECIMAL(5,2) NOT NULL ,
  `unidadesxcaja` TINYINT(6) NOT NULL ,
  `activo` TINYINT(1)  NOT NULL DEFAULT 1 ,
  `fechaestablecido` TIMESTAMP NULL ,
  PRIMARY KEY (`idprecioproducto`) ,
  INDEX `fk_preciosproducto_productos` (`idproducto` ASC) ,
  CONSTRAINT `fk_preciosproducto_productos`
    FOREIGN KEY (`idproducto` )
    REFERENCES `misimportaciones`.`productos` (`idproducto` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `misimportaciones`.`personas`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `misimportaciones`.`personas` (
  `idpersona` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(45) NOT NULL ,
  `escliente` TINYINT(1)  NOT NULL ,
  PRIMARY KEY (`idpersona`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `misimportaciones`.`tiposdoc`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `misimportaciones`.`tiposdoc` (
  `idtipodoc` INT NOT NULL AUTO_INCREMENT ,
  `nombre` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`idtipodoc`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `misimportaciones`.`documentos`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `misimportaciones`.`documentos` (
  `iddocumento` INT NOT NULL AUTO_INCREMENT ,
  `fecha` DATE NOT NULL ,
  `total` DECIMAL(6,2) NOT NULL ,
  `idpersona` INT NOT NULL ,
  `idtipodoc` INT NOT NULL ,
  `fechacreado` TIMESTAMP NOT NULL ,
  `observaciones` VARCHAR(100) NULL ,
  `referencia` VARCHAR(45) NULL ,
  PRIMARY KEY (`iddocumento`) ,
  INDEX `fk_facturas_clientes1` (`idpersona` ASC) ,
  INDEX `fk_documentos_tiposdoc1` (`idtipodoc` ASC) ,
  CONSTRAINT `fk_facturas_clientes1`
    FOREIGN KEY (`idpersona` )
    REFERENCES `misimportaciones`.`personas` (`idpersona` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_documentos_tiposdoc1`
    FOREIGN KEY (`idtipodoc` )
    REFERENCES `misimportaciones`.`tiposdoc` (`idtipodoc` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `misimportaciones`.`productosxdocumento`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `misimportaciones`.`productosxdocumento` (
  `iddocumento` INT NOT NULL ,
  `idprecioproducto` INT NOT NULL ,
  `cantidadcajas` INT NOT NULL ,
  `linea` TINYINT(3) NULL ,
  PRIMARY KEY (`iddocumento`, `idprecioproducto`) ,
  INDEX `fk_facturas_has_preciosproducto_facturas1` (`iddocumento` ASC) ,
  INDEX `fk_facturas_has_preciosproducto_preciosproducto1` (`idprecioproducto` ASC) ,
  CONSTRAINT `fk_facturas_has_preciosproducto_facturas1`
    FOREIGN KEY (`iddocumento` )
    REFERENCES `misimportaciones`.`documentos` (`iddocumento` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_facturas_has_preciosproducto_preciosproducto1`
    FOREIGN KEY (`idprecioproducto` )
    REFERENCES `misimportaciones`.`preciosproducto` (`idprecioproducto` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Placeholder table for view `misimportaciones`.`vw_articulos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `misimportaciones`.`vw_articulos` (`categoria` INT, `descripcion` INT, `precio` INT, `unidadesxcaja` INT, `cajas` INT, `idprecioproducto` INT);

-- -----------------------------------------------------
-- View `misimportaciones`.`vw_articulos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `misimportaciones`.`vw_articulos`;
USE `misimportaciones`;
CREATE  OR REPLACE VIEW vw_articulos AS
SELECT
c.nombre as categoria,
CONCAT(m.nombre," ", IF (p.contenido IS NULL,"",p.contenido)) as descripcion,
pp.precio,
pp.unidadesxcaja,
SUM(cantidadcajas) as cajas,
pp.idprecioproducto
FROM productos p
JOIN categorias c ON c.idcategoria = p.idcategoria
JOIN marcas m ON m.idmarca = p.idmarca
JOIN preciosproducto pp ON pp.idproducto = p.idproducto AND pp.activo =1
LEFT JOIN productosxdocumento pd ON pp.idprecioproducto = pd.idprecioproducto
LEFT JOIN documentos d ON d.iddocumento = pd.iddocumento AND d.idtipodoc IN (1,2)
WHERE p.activo = 1
GROUP BY p.idproducto
;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `misimportaciones`.`marcas`
-- -----------------------------------------------------
SET AUTOCOMMIT=0;
USE `misimportaciones`;
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('1', 'Kent');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('2', 'Nicole');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('3', 'Jou Jou');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('4', 'Aloe Vera');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('5', 'Trigo y Miel');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('6', 'Placenta');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('7', 'Stefania');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('8', 'Murcia');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('9', 'Scooby-Doo');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('10', 'Miskenass');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('11', 'Gardenia');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('12', 'Soraya');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('13', 'Tebby Jeans');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('14', 'Bebe Kent');
INSERT INTO `misimportaciones`.`marcas` (`idmarca`, `nombre`) VALUES ('15', 'Jeannette');

COMMIT;

-- -----------------------------------------------------
-- Data for table `misimportaciones`.`categorias`
-- -----------------------------------------------------
SET AUTOCOMMIT=0;
USE `misimportaciones`;
INSERT INTO `misimportaciones`.`categorias` (`idcategoria`, `nombre`) VALUES ('1', 'Champu');
INSERT INTO `misimportaciones`.`categorias` (`idcategoria`, `nombre`) VALUES ('2', 'Crema');
INSERT INTO `misimportaciones`.`categorias` (`idcategoria`, `nombre`) VALUES ('3', 'Estuche');
INSERT INTO `misimportaciones`.`categorias` (`idcategoria`, `nombre`) VALUES ('4', 'Talco');
INSERT INTO `misimportaciones`.`categorias` (`idcategoria`, `nombre`) VALUES ('5', 'Talquera');
INSERT INTO `misimportaciones`.`categorias` (`idcategoria`, `nombre`) VALUES ('6', 'Fijador');
INSERT INTO `misimportaciones`.`categorias` (`idcategoria`, `nombre`) VALUES ('7', 'Desodrante');

COMMIT;

-- -----------------------------------------------------
-- Data for table `misimportaciones`.`productos`
-- -----------------------------------------------------
SET AUTOCOMMIT=0;
USE `misimportaciones`;
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('1', '1', '1', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('2', '1', '2', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('3', '1', '3', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('4', '1', '4', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('5', '1', '5', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('6', '1', '6', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('7', '1', '7', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('8', '1', '8', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('9', '1', '9', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('10', '1', '10', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('11', '2', '7', '16onz', 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('12', '2', '7', '24onz', 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('13', '2', '11', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('14', '2', '12', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('15', '3', '3', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('16', '3', '13', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('17', '4', '14', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('18', '5', '7', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('19', '5', '15', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('20', '6', '7', NULL, 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('21', '7', '1', 'Rolon', 1);
INSERT INTO `misimportaciones`.`productos` (`idproducto`, `idcategoria`, `idmarca`, `contenido`, `activo`) VALUES ('22', '7', '1', 'Spray', 1);

COMMIT;

-- -----------------------------------------------------
-- Data for table `misimportaciones`.`preciosproducto`
-- -----------------------------------------------------
SET AUTOCOMMIT=0;
USE `misimportaciones`;
INSERT INTO `misimportaciones`.`preciosproducto` (`idprecioproducto`, `idproducto`, `precio`, `unidadesxcaja`, `activo`, `fechaestablecido`) VALUES ('1', '1', '25', '24', 1, NULL);

COMMIT;

-- -----------------------------------------------------
-- Data for table `misimportaciones`.`tiposdoc`
-- -----------------------------------------------------
SET AUTOCOMMIT=0;
USE `misimportaciones`;
INSERT INTO `misimportaciones`.`tiposdoc` (`idtipodoc`, `nombre`) VALUES ('1', 'FACTURA');
INSERT INTO `misimportaciones`.`tiposdoc` (`idtipodoc`, `nombre`) VALUES ('2', 'POLIZA');
INSERT INTO `misimportaciones`.`tiposdoc` (`idtipodoc`, `nombre`) VALUES ('3', 'PEDIDO');

COMMIT;
