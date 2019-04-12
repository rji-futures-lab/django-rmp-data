SELECT "rmp_tbls1processchemicals"."ProcessChemicalID", "rmp_tbls1processchemicals"."ProcessID", "rmp_tbls1processchemicals"."ChemicalID", "rmp_tbls1processchemicals"."Quantity", "rmp_tbls1processchemicals"."CBI_Flag", "rmp_tbls1processchemicals"."ProcessChemicalID" AS "procchem_id", "rmp_tbls1processchemicals"."ProcessID" AS "process_id", "rmp_tbls1processchemicals"."ChemicalID" AS "chemical_id", ("rmp_tbls1processchemicals"."Quantity")::bigint AS "quantity_lbs", "rmp_tbls1processchemicals"."CBI_Flag" AS "cbi_flag", COUNT("rmp_tbls5flammablesaltreleases"."FlammableID") AS "num_alt_flam", COUNT("rmp_tbls3toxicsaltreleases"."ToxicID") AS "num_alt_tox", COUNT("rmp_tbls8_prevention_program_chemicals"."PrimaryKey") AS "num_prevent_2_chem", COUNT("rmp_tbls7_prevention_program_chemicals"."PrimaryKey") AS "num_prevent_3_chem", COUNT("rmp_tbls1flammablemixturechemicals"."FlamMixChemID") AS "num_proc_flam", COUNT("rmp_tbls4flammablesworstcase"."FlammableID") AS "num_worst_flam", COUNT("rmp_tbls2toxicsworstcase"."ToxicID") AS "num_worst_tox", "rmp_tlkpchemicals"."CASNumber" AS "cas", "rmp_tlkpchemicals"."ChemType" AS "chemical_type", "rmp_tlkpchemicals"."ChemicalName" AS "chemical_name", "rmp_tlkpchemicals"."ChemicalID", "rmp_tlkpchemicals"."ChemicalName", "rmp_tlkpchemicals"."CASNumber", "rmp_tlkpchemicals"."Threshold", "rmp_tlkpchemicals"."ChemType", "rmp_tlkpchemicals"."flgCBI", "rmp_tlkpchemicals"."ChemOwner" FROM "rmp_tbls1processchemicals" INNER JOIN "rmp_tlkpchemicals" ON ("rmp_tbls1processchemicals"."ChemicalID" = "rmp_tlkpchemicals"."ChemicalID") LEFT OUTER JOIN "rmp_tbls5flammablesaltreleases" ON ("rmp_tbls1processchemicals"."ProcessChemicalID" = "rmp_tbls5flammablesaltreleases"."ProcessChemicalID") LEFT OUTER JOIN "rmp_tbls3toxicsaltreleases" ON ("rmp_tbls1processchemicals"."ProcessChemicalID" = "rmp_tbls3toxicsaltreleases"."ProcessChemicalID") LEFT OUTER JOIN "rmp_tbls8_prevention_program_chemicals" ON ("rmp_tbls1processchemicals"."ProcessChemicalID" = "rmp_tbls8_prevention_program_chemicals"."ProcessChemicalID") LEFT OUTER JOIN "rmp_tbls7_prevention_program_chemicals" ON ("rmp_tbls1processchemicals"."ProcessChemicalID" = "rmp_tbls7_prevention_program_chemicals"."ProcessChemicalID") LEFT OUTER JOIN "rmp_tbls1flammablemixturechemicals" ON ("rmp_tbls1processchemicals"."ProcessChemicalID" = "rmp_tbls1flammablemixturechemicals"."ProcessChemicalID") LEFT OUTER JOIN "rmp_tbls4flammablesworstcase" ON ("rmp_tbls1processchemicals"."ProcessChemicalID" = "rmp_tbls4flammablesworstcase"."ProcessChemicalID") LEFT OUTER JOIN "rmp_tbls2toxicsworstcase" ON ("rmp_tbls1processchemicals"."ProcessChemicalID" = "rmp_tbls2toxicsworstcase"."ProcessChemicalID") GROUP BY "rmp_tbls1processchemicals"."ProcessChemicalID", ("rmp_tbls1processchemicals"."Quantity")::bigint, "rmp_tlkpchemicals"."ChemicalID"




--
-- Table structure for table `rmp_acc_chem`
--

DROP TABLE IF EXISTS `rmp_acc_chem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_acc_chem` (
  `accchem_id` int(11) DEFAULT NULL,
  `accident_id` int(11) DEFAULT NULL,
  `chemical_id` int(11) DEFAULT NULL,
  `quantity_lbs` double DEFAULT NULL,
  `percent_weight` float DEFAULT NULL,
  `num_acc_flam` int(11) DEFAULT NULL,
  `cas` char(9) DEFAULT NULL,
  `chemical_type` char(1) DEFAULT NULL,
  UNIQUE KEY `rmpind_19` (`accchem_id`),
  KEY `rmpj08` (`accident_id`),
  KEY `rmpind_12` (`accident_id`,`quantity_lbs`),
  KEY `rmpind_13` (`cas`),
  KEY `rmp301` (`chemical_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_acc_flam`
--

DROP TABLE IF EXISTS `rmp_acc_flam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_acc_flam` (
  `flammixchem_id` int(11) DEFAULT NULL,
  `accchem_id` int(11) DEFAULT NULL,
  `chemical_id` int(11) DEFAULT NULL,
  UNIQUE KEY `rmpu06` (`flammixchem_id`),
  KEY `rmpj07` (`accchem_id`),
  KEY `rmp302` (`chemical_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_accident`
--

DROP TABLE IF EXISTS `rmp_accident`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_accident` (
  `accident_id` int(11) DEFAULT NULL,
  `rmp_id` bigint(20) DEFAULT NULL,
  `accident_date` varchar(25) DEFAULT NULL,
  `accident_time` char(4) DEFAULT NULL,
  `naics` char(6) DEFAULT NULL,
  `release_duration` char(5) DEFAULT NULL,
  `re_gas` char(1) DEFAULT NULL,
  `re_spill` char(1) DEFAULT NULL,
  `re_fire` char(1) DEFAULT NULL,
  `re_explosion` char(1) DEFAULT NULL,
  `re_reactiveincid` char(1) DEFAULT NULL,
  `rs_storagevessel` char(1) DEFAULT NULL,
  `rs_piping` char(1) DEFAULT NULL,
  `rs_processvessel` char(1) DEFAULT NULL,
  `rs_transferhose` char(1) DEFAULT NULL,
  `rs_valve` char(1) DEFAULT NULL,
  `rs_pump` char(1) DEFAULT NULL,
  `rs_joint` char(1) DEFAULT NULL,
  `rs_other` varchar(200) DEFAULT NULL,
  `wind_speed` float DEFAULT NULL,
  `wind_speed_unit` char(1) DEFAULT NULL,
  `wind_direction` char(3) DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  `stability_class` char(1) DEFAULT NULL,
  `precipitation_yn` char(1) DEFAULT NULL,
  `unknown_weather` char(1) DEFAULT NULL,
  `deaths_workers` int(11) DEFAULT NULL,
  `deaths_responders` int(11) DEFAULT NULL,
  `deaths_public` int(11) DEFAULT NULL,
  `injuries_workers` int(11) DEFAULT NULL,
  `injuries_respond` int(11) DEFAULT NULL,
  `injuries_public` int(11) DEFAULT NULL,
  `onsite_damage` bigint(20) DEFAULT NULL,
  `offsite_deaths` int(11) DEFAULT NULL,
  `offsite_hosp` int(11) DEFAULT NULL,
  `offsite_medical` int(11) DEFAULT NULL,
  `offsite_evacuated` int(11) DEFAULT NULL,
  `offsite_shelter` int(11) DEFAULT NULL,
  `offsite_damage` int(11) DEFAULT NULL,
  `ed_kills` char(1) DEFAULT NULL,
  `ed_defoliation` char(1) DEFAULT NULL,
  `ed_watercontam` char(1) DEFAULT NULL,
  `ed_soilcontam` char(1) DEFAULT NULL,
  `ed_other` varchar(200) DEFAULT NULL,
  `initiating_event` char(1) DEFAULT NULL,
  `cf_equipmentfail` char(1) DEFAULT NULL,
  `cf_humanerror` char(1) DEFAULT NULL,
  `cf_impprocedure` char(1) DEFAULT NULL,
  `cf_overpressure` char(1) DEFAULT NULL,
  `cf_upsetcondition` char(1) DEFAULT NULL,
  `cf_bypasscond` char(1) DEFAULT NULL,
  `cf_maintenance` char(1) DEFAULT NULL,
  `cf_processdesign` char(1) DEFAULT NULL,
  `cf_unsuitequip` char(1) DEFAULT NULL,
  `cf_unusualweather` char(1) DEFAULT NULL,
  `cf_management` char(1) DEFAULT NULL,
  `cf_other` varchar(200) DEFAULT NULL,
  `offsite_notify` varchar(25) DEFAULT NULL,
  `ci_improveequip` char(1) DEFAULT NULL,
  `ci_revisedmaint` char(1) DEFAULT NULL,
  `ci_revisedtrain` char(1) DEFAULT NULL,
  `ci_opprocedures` char(1) DEFAULT NULL,
  `ci_processcontrol` char(1) DEFAULT NULL,
  `ci_mitigationsys` char(1) DEFAULT NULL,
  `ci_responseplan` char(1) DEFAULT NULL,
  `ci_changedprocess` char(1) DEFAULT NULL,
  `ci_reducedinv` char(1) DEFAULT NULL,
  `ci_none` char(1) DEFAULT NULL,
  `ci_other` varchar(200) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  `num_acc_chem` int(11) DEFAULT NULL,
  `flam_tot` double DEFAULT NULL,
  `toxic_tot` double DEFAULT NULL,
  `quantity_tot` double DEFAULT NULL,
  `num_deaths` int(11) DEFAULT NULL,
  `num_injuries` int(11) DEFAULT NULL,
  `num_evacuated` int(11) DEFAULT NULL,
  `property_damage` bigint(20) DEFAULT NULL,
  `env_damage` char(1) DEFAULT NULL,
  UNIQUE KEY `rmpind_17` (`accident_id`),
  KEY `rmpj09` (`rmp_id`),
  KEY `rmpind_31` (`rmp_id`,`accident_date`),
  KEY `rmpind_32` (`naics`),
  KEY `rmpind_33` (`num_deaths`,`num_injuries`,`num_evacuated`,`property_damage`),
  KEY `rmpind_34` (`rmp_id`,`num_deaths`,`num_injuries`,`num_evacuated`,`property_damage`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_alt_flam`
--

DROP TABLE IF EXISTS `rmp_alt_flam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_alt_flam` (
  `flammable_id` int(11) DEFAULT NULL,
  `procchem_id` int(11) DEFAULT NULL,
  `analytical_basis` varchar(255) DEFAULT NULL,
  `scenario` varchar(200) DEFAULT NULL,
  `quantity_lbs` double DEFAULT NULL,
  `endpoint_used` varchar(30) DEFAULT NULL,
  `lfl_value` float DEFAULT NULL,
  `endpoint_distance` float DEFAULT NULL,
  `population` varchar(9) DEFAULT NULL,
  `pr_schools` char(1) DEFAULT NULL,
  `pr_residences` char(1) DEFAULT NULL,
  `pr_hospitals` char(1) DEFAULT NULL,
  `pr_prisons` char(1) DEFAULT NULL,
  `pr_public_rec` char(1) DEFAULT NULL,
  `pr_comm_ind` char(1) DEFAULT NULL,
  `pr_othertype` varchar(200) DEFAULT NULL,
  `er_natlstateparks` char(1) DEFAULT NULL,
  `er_wildlifesanct` char(1) DEFAULT NULL,
  `er_fedwilderness` char(1) DEFAULT NULL,
  `er_othertype` varchar(200) DEFAULT NULL,
  `pm_dikes` char(1) DEFAULT NULL,
  `pm_firewalls` char(1) DEFAULT NULL,
  `pm_blastwalls` char(1) DEFAULT NULL,
  `pm_enclosures` char(1) DEFAULT NULL,
  `pm_othertype` varchar(200) DEFAULT NULL,
  `am_sprinklers` char(1) DEFAULT NULL,
  `am_delugesystems` char(1) DEFAULT NULL,
  `am_watercurtain` char(1) DEFAULT NULL,
  `am_excessflowvalve` char(1) DEFAULT NULL,
  `am_othertype` varchar(200) DEFAULT NULL,
  `ptrgraphic` varchar(12) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  UNIQUE KEY `rmpu04` (`flammable_id`),
  KEY `rmpj15` (`procchem_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_alt_tox`
--

DROP TABLE IF EXISTS `rmp_alt_tox`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_alt_tox` (
  `toxic_id` int(11) DEFAULT NULL,
  `procchem_id` int(11) DEFAULT NULL,
  `percent_weight` float DEFAULT NULL,
  `physical_state` char(1) DEFAULT NULL,
  `analytical_basis` varchar(255) DEFAULT NULL,
  `scenario` varchar(200) DEFAULT NULL,
  `quantity_lbs` double DEFAULT NULL,
  `release_duration` float DEFAULT NULL,
  `release_rate` float DEFAULT NULL,
  `wind_speed` float DEFAULT NULL,
  `stability_class` char(1) DEFAULT NULL,
  `topography` char(1) DEFAULT NULL,
  `endpoint_distance` float DEFAULT NULL,
  `population` varchar(9) DEFAULT NULL,
  `pr_schools` char(1) DEFAULT NULL,
  `pr_residences` char(1) DEFAULT NULL,
  `pr_hospitals` char(1) DEFAULT NULL,
  `pr_prisons` char(1) DEFAULT NULL,
  `pr_public_rec` char(1) DEFAULT NULL,
  `pr_comm_ind` char(1) DEFAULT NULL,
  `pr_othertype` varchar(200) DEFAULT NULL,
  `er_natlstateparks` char(1) DEFAULT NULL,
  `er_wildlifesanct` char(1) DEFAULT NULL,
  `er_fedwilderness` char(1) DEFAULT NULL,
  `er_othertype` varchar(200) DEFAULT NULL,
  `pm_dikes` char(1) DEFAULT NULL,
  `pm_enclosures` char(1) DEFAULT NULL,
  `pm_berms` char(1) DEFAULT NULL,
  `pm_drains` char(1) DEFAULT NULL,
  `pm_sumps` char(1) DEFAULT NULL,
  `pm_othertype` varchar(200) DEFAULT NULL,
  `am_sprinklers` char(1) DEFAULT NULL,
  `am_delugesystems` char(1) DEFAULT NULL,
  `am_watercurtain` char(1) DEFAULT NULL,
  `am_neutralization` char(1) DEFAULT NULL,
  `am_excessflowvalve` char(1) DEFAULT NULL,
  `am_flares` char(1) DEFAULT NULL,
  `am_scrubbers` char(1) DEFAULT NULL,
  `am_emerg_shutdown` char(1) DEFAULT NULL,
  `am_othertype` varchar(200) DEFAULT NULL,
  `ptrgraphic` varchar(12) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  UNIQUE KEY `rmpu02` (`toxic_id`),
  KEY `rmpj13` (`procchem_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_chem_cd`
--

DROP TABLE IF EXISTS `rmp_chem_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_chem_cd` (
  `chemical_id` int(11) DEFAULT NULL,
  `chemical_name` varchar(100) DEFAULT NULL,
  `cas2` char(10) DEFAULT NULL,
  `threshold` float DEFAULT NULL,
  `chemical_type` char(1) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  `chemical_owner` char(3) DEFAULT NULL,
  UNIQUE KEY `ind1` (`chemical_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_cities`
--

DROP TABLE IF EXISTS `rmp_cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_cities` (
  `city` varchar(30) DEFAULT NULL,
  `state` char(2) DEFAULT NULL,
  `num_fac` int(11) DEFAULT NULL,
  UNIQUE KEY `ind01` (`city`,`state`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_dereg_cd`
--

DROP TABLE IF EXISTS `rmp_dereg_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_dereg_cd` (
  `dereg` char(2) DEFAULT NULL,
  `dereg_tr` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_dochan_cd`
--

DROP TABLE IF EXISTS `rmp_dochan_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_dochan_cd` (
  `dochan` char(1) DEFAULT NULL,
  `dochan_tr` varchar(50) DEFAULT NULL,
  UNIQUE KEY `ind1` (`dochan`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_doctyp_cd`
--

DROP TABLE IF EXISTS `rmp_doctyp_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_doctyp_cd` (
  `doctyp` char(1) DEFAULT NULL,
  `doctyp_tr` varchar(50) DEFAULT NULL,
  UNIQUE KEY `ind1` (`doctyp`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_events_cd`
--

DROP TABLE IF EXISTS `rmp_events_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_events_cd` (
  `events` char(1) DEFAULT NULL,
  `events_tr` varchar(50) DEFAULT NULL,
  UNIQUE KEY `ind1` (`events`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_exec_sum`
--

DROP TABLE IF EXISTS `rmp_exec_sum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_exec_sum` (
  `exec_seq_num` int(11) DEFAULT NULL,
  `rmp_id` bigint(20) DEFAULT NULL,
  `seq_num` int(11) DEFAULT NULL,
  `line` mediumtext,
  UNIQUE KEY `ind1` (`rmp_id`,`exec_seq_num`,`seq_num`),
  UNIQUE KEY `ind2` (`seq_num`),
  FULLTEXT KEY `fl1` (`line`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_exec_sum_len`
--

DROP TABLE IF EXISTS `rmp_exec_sum_len`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_exec_sum_len` (
  `rmp_id` int(11) DEFAULT NULL,
  `byte_count` int(11) DEFAULT NULL,
  `suspect_count` int(11) DEFAULT NULL,
  `line_count` int(11) DEFAULT NULL,
  `edited_yn` char(1) DEFAULT 'n',
  UNIQUE KEY `ind1` (`rmp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_execsum`
--

DROP TABLE IF EXISTS `rmp_execsum`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_execsum` (
  `rmp_id` int(11) DEFAULT NULL,
  `execsum` mediumtext,
  UNIQUE KEY `ind1` (`rmp_id`),
  FULLTEXT KEY `ind2` (`execsum`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_facility`
--

DROP TABLE IF EXISTS `rmp_facility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_facility` (
  `facility_id` char(12) DEFAULT NULL,
  `facility_name` varchar(250) DEFAULT NULL,
  `marplot_id` varchar(16) DEFAULT NULL,
  `cameo_id` varchar(10) DEFAULT NULL,
  `rmp_id` bigint(20) DEFAULT NULL,
  `street_1` varchar(50) DEFAULT NULL,
  `street_2` varchar(35) DEFAULT NULL,
  `city` varchar(19) DEFAULT NULL,
  `state` char(2) DEFAULT NULL,
  `zip` varchar(5) DEFAULT NULL,
  `zip_ext` varchar(4) DEFAULT NULL,
  `county_fips` varchar(5) DEFAULT NULL,
  `num_registrations` int(11) DEFAULT NULL,
  `latitude_dec` char(10) DEFAULT NULL,
  `longitude_dec` char(11) DEFAULT NULL,
  `num_registration` int(11) DEFAULT NULL,
  `sub_type` char(1) DEFAULT NULL,
  `sub_date` date DEFAULT NULL,
  `exec_type` char(1) DEFAULT NULL,
  `execsum_rmp_id` int(11) DEFAULT NULL,
  `exec_sub_type` char(1) DEFAULT NULL,
  `exec_sub_date` date DEFAULT NULL,
  `deregistration_date` date DEFAULT NULL,
  `dereg_effect_date` date DEFAULT NULL,
  `parent` varchar(50) DEFAULT NULL,
  `parent_2` varchar(50) DEFAULT NULL,
  `operator_name` varchar(35) DEFAULT NULL,
  `operator_city` varchar(20) DEFAULT NULL,
  `operator_state` char(2) DEFAULT NULL,
  `operator_zip` char(5) DEFAULT NULL,
  `province` varchar(35) DEFAULT NULL,
  `county` varchar(60) DEFAULT NULL,
  `country` varchar(50) DEFAULT NULL,
  `sub_reason` char(3) DEFAULT NULL,
  `dereg_reason` char(2) DEFAULT NULL,
  `dereg_other` varchar(80) DEFAULT NULL,
  `toxic_tot` double DEFAULT NULL,
  `flam_tot` double DEFAULT NULL,
  `quantity_tot` double DEFAULT NULL,
  `num_proc_23` int(11) DEFAULT NULL,
  `toxic_tot_23` double DEFAULT NULL,
  `flam_tot_23` double DEFAULT NULL,
  `quantity_tot_23` double DEFAULT NULL,
  `all_naics` varchar(100) DEFAULT NULL,
  `sortid_1` int(11) DEFAULT NULL,
  `sortid_2` int(11) DEFAULT NULL,
  `sortid_3` int(11) DEFAULT NULL,
  `deregistration_yn` char(1) DEFAULT 'n',
  `num_fte` int(11) DEFAULT NULL,
  `num_accident` int(11) DEFAULT NULL,
  `acc_flam_tot` double DEFAULT NULL,
  `acc_toxic_tot` double DEFAULT NULL,
  `acc_quantity_tot` double DEFAULT NULL,
  `num_deaths` int(11) DEFAULT NULL,
  `num_injuries` int(11) DEFAULT NULL,
  `num_evacuated` int(11) DEFAULT NULL,
  `property_damage` bigint(20) DEFAULT NULL,
  UNIQUE KEY `rmpu10` (`facility_id`),
  UNIQUE KEY `rmpu11` (`rmp_id`),
  UNIQUE KEY `srt1` (`sortid_1`),
  UNIQUE KEY `srt2` (`sortid_2`),
  UNIQUE KEY `srt3` (`sortid_3`),
  UNIQUE KEY `rmp316` (`execsum_rmp_id`),
  KEY `rmp303` (`county`,`state`),
  KEY `rmp304` (`city`,`state`),
  KEY `rmp305` (`country`),
  KEY `rmp308` (`state`),
  KEY `rmp309` (`zip`,`state`),
  KEY `indado1` (`facility_name`),
  FULLTEXT KEY `rmp306` (`facility_name`),
  FULLTEXT KEY `rmp307` (`facility_name`,`operator_name`),
  FULLTEXT KEY `rmp314` (`all_naics`),
  FULLTEXT KEY `rmp315` (`parent`,`parent_2`),
  FULLTEXT KEY `if01` (`facility_name`,`operator_name`,`parent`,`parent_2`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_lepc`
--

DROP TABLE IF EXISTS `rmp_lepc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_lepc` (
  `lepc_id` varchar(6) DEFAULT NULL,
  `facility_id` varchar(12) DEFAULT NULL,
  `state` char(2) DEFAULT NULL,
  `facility_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_lepc_cd`
--

DROP TABLE IF EXISTS `rmp_lepc_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_lepc_cd` (
  `lepc_id` char(6) DEFAULT NULL,
  `lepc_name` varchar(43) DEFAULT NULL,
  `state` char(2) DEFAULT NULL,
  UNIQUE KEY `ind1` (`lepc_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_lldesc_cd`
--

DROP TABLE IF EXISTS `rmp_lldesc_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_lldesc_cd` (
  `lldesc` char(2) DEFAULT NULL,
  `lldesc_tr` varchar(40) DEFAULT NULL,
  UNIQUE KEY `ind1` (`lldesc`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_llmeth_cd`
--

DROP TABLE IF EXISTS `rmp_llmeth_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_llmeth_cd` (
  `primary_key` int(11) DEFAULT NULL,
  `llmeth` char(2) DEFAULT NULL,
  `llmeth_tr` varchar(100) DEFAULT NULL,
  UNIQUE KEY `ind1` (`llmeth`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_phys_cd`
--

DROP TABLE IF EXISTS `rmp_phys_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_phys_cd` (
  `phys` char(1) DEFAULT NULL,
  `phys_tr` varchar(30) DEFAULT NULL,
  UNIQUE KEY `ind1` (`phys`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_prev2_text`
--

DROP TABLE IF EXISTS `rmp_prev2_text`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_prev2_text` (
  `prevent_2_id` int(11) DEFAULT NULL,
  `seq_num` int(11) DEFAULT NULL,
  `line` mediumtext,
  UNIQUE KEY `ind1` (`prevent_2_id`,`seq_num`),
  UNIQUE KEY `ind2` (`seq_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_prev2text`
--

DROP TABLE IF EXISTS `rmp_prev2text`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_prev2text` (
  `prevent_2_id` int(11) DEFAULT NULL,
  `desctext` mediumtext,
  UNIQUE KEY `ind1` (`prevent_2_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_prev3_text`
--

DROP TABLE IF EXISTS `rmp_prev3_text`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_prev3_text` (
  `prevent_3_id` int(11) DEFAULT NULL,
  `seq_num` int(11) DEFAULT NULL,
  `line` mediumtext,
  UNIQUE KEY `ind1` (`prevent_3_id`,`seq_num`),
  UNIQUE KEY `ind2` (`seq_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_prev3text`
--

DROP TABLE IF EXISTS `rmp_prev3text`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_prev3text` (
  `prevent_3_id` int(11) DEFAULT NULL,
  `desctext` mediumtext,
  UNIQUE KEY `ind1` (`prevent_3_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_prevent_2`
--

DROP TABLE IF EXISTS `rmp_prevent_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_prevent_2` (
  `prevent_2_id` int(11) DEFAULT NULL,
  `procnaics_id` int(11) DEFAULT NULL,
  `safety_info_date` char(11) DEFAULT NULL,
  `fr_nfpa58` char(1) DEFAULT NULL,
  `fr_osha` char(1) DEFAULT NULL,
  `fr_astm` char(1) DEFAULT NULL,
  `fr_ansi` char(1) DEFAULT NULL,
  `fr_asme` char(1) DEFAULT NULL,
  `fr_none` char(1) DEFAULT NULL,
  `fr_other` varchar(200) DEFAULT NULL,
  `fr_comments` varchar(100) DEFAULT NULL,
  `haz_review_date` char(11) DEFAULT NULL,
  `change_comp_date` char(11) DEFAULT NULL,
  `mh_toxicrelease` char(1) DEFAULT NULL,
  `mh_fire` char(1) DEFAULT NULL,
  `mh_explosion` char(1) DEFAULT NULL,
  `mh_runawayreact` char(1) DEFAULT NULL,
  `mh_polymerization` char(1) DEFAULT NULL,
  `mh_overpressure` char(1) DEFAULT NULL,
  `mh_corrosion` char(1) DEFAULT NULL,
  `mh_overfilling` char(1) DEFAULT NULL,
  `mh_contamination` char(1) DEFAULT NULL,
  `mh_equipfailure` char(1) DEFAULT NULL,
  `mh_cooling_loss` char(1) DEFAULT NULL,
  `mh_earthquake` char(1) DEFAULT NULL,
  `mh_floods` char(1) DEFAULT NULL,
  `mh_tornado` char(1) DEFAULT NULL,
  `mh_hurricanes` char(1) DEFAULT NULL,
  `mh_othertype` varchar(200) DEFAULT NULL,
  `pc_vents` char(1) DEFAULT NULL,
  `pc_reliefvalves` char(1) DEFAULT NULL,
  `pc_checkvalves` char(1) DEFAULT NULL,
  `pc_scrubbers` char(1) DEFAULT NULL,
  `pc_flares` char(1) DEFAULT NULL,
  `pc_manualshutoffs` char(1) DEFAULT NULL,
  `pc_autoshutoffs` char(1) DEFAULT NULL,
  `pc_interlocks` char(1) DEFAULT NULL,
  `pc_alarms` char(1) DEFAULT NULL,
  `pc_keyedbypass` char(1) DEFAULT NULL,
  `pc_emergencyair` char(1) DEFAULT NULL,
  `pc_emergencypower` char(1) DEFAULT NULL,
  `pc_backuppump` char(1) DEFAULT NULL,
  `pc_groundingequip` char(1) DEFAULT NULL,
  `pc_inhibitoradd` char(1) DEFAULT NULL,
  `pc_rupturedisks` char(1) DEFAULT NULL,
  `pc_excessflowdev` char(1) DEFAULT NULL,
  `pc_quenchsystem` char(1) DEFAULT NULL,
  `pc_purgesystem` char(1) DEFAULT NULL,
  `pc_none` char(1) DEFAULT NULL,
  `pc_other` varchar(200) DEFAULT NULL,
  `ms_sprinklersys` char(1) DEFAULT NULL,
  `ms_dikes` char(1) DEFAULT NULL,
  `ms_firewalls` char(1) DEFAULT NULL,
  `ms_blastwalls` char(1) DEFAULT NULL,
  `ms_delugesystem` char(1) DEFAULT NULL,
  `ms_watercurtain` char(1) DEFAULT NULL,
  `ms_enclosure` char(1) DEFAULT NULL,
  `ms_neutralization` char(1) DEFAULT NULL,
  `ms_none` char(1) DEFAULT NULL,
  `ms_other` varchar(200) DEFAULT NULL,
  `md_processarea` char(1) DEFAULT NULL,
  `md_perimetermon` char(1) DEFAULT NULL,
  `md_none` char(1) DEFAULT NULL,
  `md_other` varchar(200) DEFAULT NULL,
  `ch_reduceinv` char(1) DEFAULT NULL,
  `ch_increaseinv` char(1) DEFAULT NULL,
  `ch_changeparam` char(1) DEFAULT NULL,
  `ch_proccontrol` char(1) DEFAULT NULL,
  `ch_procdetect` char(1) DEFAULT NULL,
  `ch_perimetermon` char(1) DEFAULT NULL,
  `ch_mitigationsys` char(1) DEFAULT NULL,
  `ch_nonerequired` char(1) DEFAULT NULL,
  `ch_none` char(1) DEFAULT NULL,
  `ch_other` varchar(200) DEFAULT NULL,
  `proc_review_date` char(11) DEFAULT NULL,
  `train_review_date` char(11) DEFAULT NULL,
  `tr_classroom` char(1) DEFAULT NULL,
  `tr_onthejob` char(1) DEFAULT NULL,
  `tr_other` varchar(200) DEFAULT NULL,
  `ct_writtentest` char(1) DEFAULT NULL,
  `ct_oraltest` char(1) DEFAULT NULL,
  `ct_demonstration` char(1) DEFAULT NULL,
  `ct_observation` char(1) DEFAULT NULL,
  `ct_other` varchar(200) DEFAULT NULL,
  `maint_review_date` char(11) DEFAULT NULL,
  `maint_inspect_date` char(11) DEFAULT NULL,
  `equip_tested` varchar(200) DEFAULT NULL,
  `comp_audit_date` char(11) DEFAULT NULL,
  `audit_comp_date` char(11) DEFAULT NULL,
  `inc_invest_date` char(11) DEFAULT NULL,
  `inc_change_date` char(11) DEFAULT NULL,
  `most_recent_date` char(11) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  `num_prevent_2_chem` int(11) DEFAULT NULL,
  `num_prev2text` int(11) DEFAULT NULL,
  `num_prev2_text` int(11) DEFAULT NULL,
  UNIQUE KEY `rmpind_36` (`prevent_2_id`),
  KEY `rmpj05` (`procnaics_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_prevent_2_chem`
--

DROP TABLE IF EXISTS `rmp_prevent_2_chem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_prevent_2_chem` (
  `primary_key` int(11) DEFAULT NULL,
  `prevent_2_id` int(11) DEFAULT NULL,
  `procchem_id` int(11) DEFAULT NULL,
  UNIQUE KEY `rmpu07` (`primary_key`),
  KEY `rmpj01` (`prevent_2_id`),
  KEY `rmpj03` (`procchem_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_prevent_3`
--

DROP TABLE IF EXISTS `rmp_prevent_3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_prevent_3` (
  `prevent_3_id` int(11) DEFAULT NULL,
  `procnaics_id` int(11) DEFAULT NULL,
  `safety_info_date` char(11) DEFAULT NULL,
  `last_pha_date` char(11) DEFAULT NULL,
  `pha_whatif` char(1) DEFAULT NULL,
  `pha_checklist` char(1) DEFAULT NULL,
  `pha_whatifcheck` char(1) DEFAULT NULL,
  `pha_hazop` char(1) DEFAULT NULL,
  `pha_fmea` char(1) DEFAULT NULL,
  `pha_fta` char(1) DEFAULT NULL,
  `pha_other` varchar(200) DEFAULT NULL,
  `change_comp_date` char(11) DEFAULT NULL,
  `mh_toxicrelease` char(1) DEFAULT NULL,
  `mh_fire` char(1) DEFAULT NULL,
  `mh_explosion` char(1) DEFAULT NULL,
  `mh_runawayreact` char(1) DEFAULT NULL,
  `mh_polymerization` char(1) DEFAULT NULL,
  `mh_overpressure` char(1) DEFAULT NULL,
  `mh_corrosion` char(1) DEFAULT NULL,
  `mh_overfilling` char(1) DEFAULT NULL,
  `mh_contamination` char(1) DEFAULT NULL,
  `mh_equipfailure` char(1) DEFAULT NULL,
  `mh_cooling_loss` char(1) DEFAULT NULL,
  `mh_earthquake` char(1) DEFAULT NULL,
  `mh_floods` char(1) DEFAULT NULL,
  `mh_tornado` char(1) DEFAULT NULL,
  `mh_hurricanes` char(1) DEFAULT NULL,
  `mh_othertype` varchar(200) DEFAULT NULL,
  `pc_vents` char(1) DEFAULT NULL,
  `pc_reliefvalves` char(1) DEFAULT NULL,
  `pc_checkvalves` char(1) DEFAULT NULL,
  `pc_scrubbers` char(1) DEFAULT NULL,
  `pc_flares` char(1) DEFAULT NULL,
  `pc_manualshutoffs` char(1) DEFAULT NULL,
  `pc_autoshutoffs` char(1) DEFAULT NULL,
  `pc_interlocks` char(1) DEFAULT NULL,
  `pc_alarms` char(1) DEFAULT NULL,
  `pc_keyedbypass` char(1) DEFAULT NULL,
  `pc_emergencyair` char(1) DEFAULT NULL,
  `pc_emergencypower` char(1) DEFAULT NULL,
  `pc_backuppump` char(1) DEFAULT NULL,
  `pc_groundingequip` char(1) DEFAULT NULL,
  `pc_inhibitoradd` char(1) DEFAULT NULL,
  `pc_rupturedisks` char(1) DEFAULT NULL,
  `pc_excessflowdev` char(1) DEFAULT NULL,
  `pc_quenchsystem` char(1) DEFAULT NULL,
  `pc_purgesystem` char(1) DEFAULT NULL,
  `pc_none` char(1) DEFAULT NULL,
  `pc_other` varchar(200) DEFAULT NULL,
  `ms_sprinklersys` char(1) DEFAULT NULL,
  `ms_dikes` char(1) DEFAULT NULL,
  `ms_firewalls` char(1) DEFAULT NULL,
  `ms_blastwalls` char(1) DEFAULT NULL,
  `ms_delugesystem` char(1) DEFAULT NULL,
  `ms_watercurtain` char(1) DEFAULT NULL,
  `ms_enclosure` char(1) DEFAULT NULL,
  `ms_neutralization` char(1) DEFAULT NULL,
  `ms_none` char(1) DEFAULT NULL,
  `ms_other` varchar(200) DEFAULT NULL,
  `md_processarea` char(1) DEFAULT NULL,
  `md_perimetermon` char(1) DEFAULT NULL,
  `md_none` char(1) DEFAULT NULL,
  `md_other` varchar(200) DEFAULT NULL,
  `ch_reduceinv` char(1) DEFAULT NULL,
  `ch_increaseinv` char(1) DEFAULT NULL,
  `ch_changeparam` char(1) DEFAULT NULL,
  `ch_proccontrol` char(1) DEFAULT NULL,
  `ch_procdetect` char(1) DEFAULT NULL,
  `ch_perimetermon` char(1) DEFAULT NULL,
  `ch_mitigationsys` char(1) DEFAULT NULL,
  `ch_nonerequired` char(1) DEFAULT NULL,
  `ch_none` char(1) DEFAULT NULL,
  `ch_other` varchar(200) DEFAULT NULL,
  `proc_review_date` char(11) DEFAULT NULL,
  `train_review_date` char(11) DEFAULT NULL,
  `tr_classroom` char(1) DEFAULT NULL,
  `tr_onthejob` char(1) DEFAULT NULL,
  `tr_other` varchar(200) DEFAULT NULL,
  `ct_writtentest` char(1) DEFAULT NULL,
  `ct_oraltest` char(1) DEFAULT NULL,
  `ct_demonstration` char(1) DEFAULT NULL,
  `ct_observation` char(1) DEFAULT NULL,
  `ct_other` varchar(200) DEFAULT NULL,
  `maint_review_date` char(11) DEFAULT NULL,
  `maint_inspect_date` char(11) DEFAULT NULL,
  `equip_tested` varchar(200) DEFAULT NULL,
  `change_manage_date` char(11) DEFAULT NULL,
  `change_review_date` char(11) DEFAULT NULL,
  `prestart_rev_date` char(11) DEFAULT NULL,
  `comp_audit_date` char(11) DEFAULT NULL,
  `audit_comp_date` char(11) DEFAULT NULL,
  `inc_invest_date` char(11) DEFAULT NULL,
  `inc_change_date` char(11) DEFAULT NULL,
  `part_review_date` char(11) DEFAULT NULL,
  `hotwork_rev_date` char(11) DEFAULT NULL,
  `con_safety_date` char(11) DEFAULT NULL,
  `con_eval_date` char(11) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  `num_prevent_3_chem` int(11) DEFAULT NULL,
  `num_prev3text` int(11) DEFAULT NULL,
  `num_prev3_text` int(11) DEFAULT NULL,
  UNIQUE KEY `rmpind_40` (`prevent_3_id`),
  KEY `rmpj06` (`procnaics_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_prevent_3_chem`
--

DROP TABLE IF EXISTS `rmp_prevent_3_chem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_prevent_3_chem` (
  `primary_key` int(11) DEFAULT NULL,
  `prevent_3_id` int(11) DEFAULT NULL,
  `procchem_id` int(11) DEFAULT NULL,
  UNIQUE KEY `rmpu08` (`primary_key`),
  KEY `rmpj02` (`prevent_3_id`),
  KEY `rmpj04` (`procchem_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_proc_chem`
--

DROP TABLE IF EXISTS `rmp_proc_chem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_proc_chem` (
  `procchem_id` int(11) DEFAULT NULL,
  `process_id` int(11) DEFAULT NULL,
  `chemical_id` int(11) DEFAULT NULL,
  `quantity_lbs` double DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  `num_alt_flam` int(11) DEFAULT NULL,
  `num_alt_tox` int(11) DEFAULT NULL,
  `num_prevent_2_chem` int(11) DEFAULT NULL,
  `num_prevent_3_chem` int(11) DEFAULT NULL,
  `num_proc_flam` int(11) DEFAULT NULL,
  `num_worst_flam` int(11) DEFAULT NULL,
  `num_worst_tox` int(11) DEFAULT NULL,
  `cas` char(9) DEFAULT NULL,
  `chemical_type` char(1) DEFAULT NULL,
  UNIQUE KEY `rmpind_03` (`procchem_id`),
  KEY `rmpj16` (`process_id`),
  KEY `rmpind_12` (`process_id`,`quantity_lbs`),
  KEY `rmpind_13` (`cas`),
  KEY `rmp310` (`chemical_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_proc_flam`
--

DROP TABLE IF EXISTS `rmp_proc_flam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_proc_flam` (
  `flammixchem_id` int(11) DEFAULT NULL,
  `procchem_id` int(11) DEFAULT NULL,
  `chemical_id` int(11) DEFAULT NULL,
  UNIQUE KEY `rmpu05` (`flammixchem_id`),
  KEY `rmpj11` (`procchem_id`),
  KEY `rmp311` (`chemical_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_proc_naics`
--

DROP TABLE IF EXISTS `rmp_proc_naics`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_proc_naics` (
  `procnaics_id` int(11) DEFAULT NULL,
  `process_id` int(11) DEFAULT NULL,
  `naics` char(6) DEFAULT NULL,
  `num_prevent_2` int(11) DEFAULT NULL,
  `num_prevent_3` int(11) DEFAULT NULL,
  UNIQUE KEY `rmpu12` (`procnaics_id`),
  KEY `rmpj17` (`process_id`),
  KEY `rmp312` (`naics`),
  KEY `rmp313` (`process_id`,`naics`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_process`
--

DROP TABLE IF EXISTS `rmp_process`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_process` (
  `process_id` int(11) DEFAULT NULL,
  `process_desc` varchar(25) DEFAULT NULL,
  `rmp_id` bigint(20) DEFAULT NULL,
  `program_level` smallint(6) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  `num_proc_chem` int(11) DEFAULT NULL,
  `num_proc_naics` int(11) DEFAULT NULL,
  `num_chem_real` smallint(6) DEFAULT NULL,
  `num_chem_fake` smallint(6) DEFAULT NULL,
  `num_worst_tox` smallint(6) DEFAULT NULL,
  `num_alt_tox` smallint(6) DEFAULT NULL,
  `num_worst_flam` smallint(6) DEFAULT NULL,
  `num_alt_flam` smallint(6) DEFAULT NULL,
  `num_prev_2` smallint(6) DEFAULT NULL,
  `num_prev_3` smallint(6) DEFAULT NULL,
  `toxic_tot` double DEFAULT NULL,
  `flam_tot` double DEFAULT NULL,
  `quantity_tot` double DEFAULT NULL,
  `chem_tox_yn` char(1) DEFAULT 'n',
  `chem_flam_yn` char(1) DEFAULT 'n',
  UNIQUE KEY `rmpind_02` (`process_id`),
  KEY `rmpj18` (`rmp_id`),
  KEY `rmpind_110` (`program_level`,`process_desc`),
  KEY `rmpind_111` (`process_desc`),
  KEY `rmpind_112` (`rmp_id`,`quantity_tot`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_reg_cd`
--

DROP TABLE IF EXISTS `rmp_reg_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_reg_cd` (
  `reg` char(3) DEFAULT NULL,
  `reg_tr` varchar(150) DEFAULT NULL,
  UNIQUE KEY `rg1` (`reg`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_registration`
--

DROP TABLE IF EXISTS `rmp_registration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_registration` (
  `rmp_id` bigint(20) DEFAULT NULL,
  `facility_name` varchar(250) DEFAULT NULL,
  `street_1` varchar(35) DEFAULT NULL,
  `street_2` varchar(35) DEFAULT NULL,
  `city` varchar(19) DEFAULT NULL,
  `state` char(2) DEFAULT NULL,
  `zip` char(5) DEFAULT NULL,
  `zip_ext` char(4) DEFAULT NULL,
  `county_fips` char(5) DEFAULT NULL,
  `lepc` varchar(30) DEFAULT NULL,
  `latitude_dec` char(10) DEFAULT NULL,
  `longitude_dec` char(11) DEFAULT NULL,
  `valid_latlong` char(1) DEFAULT NULL,
  `latlong_meth` char(2) DEFAULT NULL,
  `latlong_desc` char(2) DEFAULT NULL,
  `facility_url` varchar(100) DEFAULT NULL,
  `facility_phone` varchar(10) DEFAULT NULL,
  `facility_email` varchar(100) DEFAULT NULL,
  `facility_duns` char(9) DEFAULT NULL,
  `parent` varchar(250) DEFAULT NULL,
  `parent_2` varchar(50) DEFAULT NULL,
  `parent_duns` char(9) DEFAULT NULL,
  `parent2_duns` char(9) DEFAULT NULL,
  `operator_name` varchar(250) DEFAULT NULL,
  `operator_phone` varchar(10) DEFAULT NULL,
  `op_street_1` varchar(35) DEFAULT NULL,
  `op_street_2` varchar(35) DEFAULT NULL,
  `operator_city` varchar(19) DEFAULT NULL,
  `operator_state` char(2) DEFAULT NULL,
  `operator_zip` char(5) DEFAULT NULL,
  `operator_zip_ext` char(4) DEFAULT NULL,
  `rmp_contact` varchar(35) DEFAULT NULL,
  `rmp_contact_title` varchar(250) DEFAULT NULL,
  `em_contact_name` varchar(250) DEFAULT NULL,
  `em_contact_title` varchar(35) DEFAULT NULL,
  `em_contact_phone` varchar(10) DEFAULT NULL,
  `phone_24hour` varchar(10) DEFAULT NULL,
  `phone_24hour_ext` varchar(10) DEFAULT NULL,
  `num_fte` int(11) DEFAULT NULL,
  `other_facility_id` char(15) DEFAULT NULL,
  `facility_id` char(12) DEFAULT NULL,
  `osha_psm_yn` char(1) DEFAULT NULL,
  `epcra_302_yn` char(1) DEFAULT NULL,
  `caa_title_v_yn` char(1) DEFAULT NULL,
  `caa_permit_id` varchar(15) DEFAULT NULL,
  `safety_inspect_dt` varchar(25) DEFAULT NULL,
  `safety_inspect_by` varchar(50) DEFAULT NULL,
  `osha_ranking` char(1) DEFAULT NULL,
  `predictive_file_yn` char(1) DEFAULT NULL,
  `submission_type` char(1) DEFAULT NULL,
  `rmp_desc` varchar(50) DEFAULT NULL,
  `no_accidents_yn` char(1) DEFAULT NULL,
  `foreign_province` varchar(35) DEFAULT NULL,
  `foreign_zip` varchar(14) DEFAULT NULL,
  `foreign_country` char(2) DEFAULT NULL,
  `num_fte_cbi_flag` char(1) DEFAULT NULL,
  `complete_check_dt` varchar(25) DEFAULT NULL,
  `error_report_dt` varchar(25) DEFAULT NULL,
  `receipt_date` varchar(25) DEFAULT NULL,
  `graphics_ind` char(1) DEFAULT NULL,
  `attachment_ind` char(1) DEFAULT NULL,
  `cert_rec_flag` char(1) DEFAULT NULL,
  `submit_method` varchar(50) DEFAULT NULL,
  `cbi_substant_flag` char(1) DEFAULT NULL,
  `elect_waiver_flag` char(1) DEFAULT NULL,
  `postmark_date` varchar(25) DEFAULT NULL,
  `rmp_complete_flag` char(1) DEFAULT NULL,
  `deregistration_dt` varchar(25) DEFAULT NULL,
  `dereg_effect_dt` varchar(25) DEFAULT NULL,
  `anniversary_date` varchar(25) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  `unsanitized_vers` char(1) DEFAULT NULL,
  `version_number` varchar(15) DEFAULT NULL,
  `frs_lat_dec` float DEFAULT NULL,
  `frs_long_dec` float DEFAULT NULL,
  `frs_ll_desc` varchar(40) DEFAULT NULL,
  `frs_ll_method` varchar(60) DEFAULT NULL,
  `hor_measure` varchar(6) DEFAULT NULL,
  `hor_ref` varchar(3) DEFAULT NULL,
  `source_scale` varchar(10) DEFAULT NULL,
  `em_email` varchar(100) DEFAULT NULL,
  `prep_name` varchar(70) DEFAULT NULL,
  `prep_street_1` varchar(35) DEFAULT NULL,
  `prep_street_2` varchar(35) DEFAULT NULL,
  `prep_city` varchar(30) DEFAULT NULL,
  `prep_state` char(2) DEFAULT NULL,
  `prep_zip` varchar(5) DEFAULT NULL,
  `prep_zip_ext` varchar(4) DEFAULT NULL,
  `prep_phone` varchar(10) DEFAULT NULL,
  `prep_foreign_state` varchar(35) DEFAULT NULL,
  `prep_country` char(2) DEFAULT NULL,
  `prep_foreign_zip` varchar(14) DEFAULT NULL,
  `sub_reason` char(3) DEFAULT NULL,
  `rmp_email` varchar(100) DEFAULT NULL,
  `dereg_reason` char(2) DEFAULT NULL,
  `dereg_other` varchar(80) DEFAULT NULL,
  `num_accident` int(11) DEFAULT NULL,
  `num_facility` int(11) DEFAULT NULL,
  `num_process` int(11) DEFAULT NULL,
  `num_response` int(11) DEFAULT NULL,
  `num_chem_real` smallint(6) DEFAULT NULL,
  `num_worst_tox` smallint(6) DEFAULT NULL,
  `num_alt_tox` smallint(6) DEFAULT NULL,
  `num_worst_flam` smallint(6) DEFAULT NULL,
  `num_alt_flam` smallint(6) DEFAULT NULL,
  `num_prev_2` smallint(6) DEFAULT NULL,
  `num_prev_3` smallint(6) DEFAULT NULL,
  `toxic_tot` double DEFAULT NULL,
  `flam_tot` double DEFAULT NULL,
  `quantity_tot` double DEFAULT NULL,
  `acc_flam_tot` double DEFAULT NULL,
  `acc_toxic_tot` double DEFAULT NULL,
  `acc_quantity_tot` double DEFAULT NULL,
  `num_deaths` int(11) DEFAULT NULL,
  `num_injuries` int(11) DEFAULT NULL,
  `num_evacuated` int(11) DEFAULT NULL,
  `property_damage` bigint(20) DEFAULT NULL,
  `county` varchar(60) DEFAULT NULL,
  `foreign_country_tr` varchar(50) DEFAULT NULL,
  `num_proc_23` smallint(6) DEFAULT NULL,
  `toxic_tot_23` double DEFAULT NULL,
  `flam_tot_23` double DEFAULT NULL,
  `quantity_tot_23` double DEFAULT NULL,
  `num_execsum_mod` smallint(6) DEFAULT NULL,
  `execsum_type` char(1) DEFAULT NULL,
  `num_execsum` int(11) DEFAULT NULL,
  `num_exec_sum` int(11) DEFAULT NULL,
  UNIQUE KEY `rmpreg3` (`rmp_id`),
  KEY `rmpj19` (`facility_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_reject_cd`
--

DROP TABLE IF EXISTS `rmp_reject_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_reject_cd` (
  `reject` char(1) DEFAULT NULL,
  `reject_tr` varchar(60) DEFAULT NULL,
  UNIQUE KEY `ind1` (`reject`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_response`
--

DROP TABLE IF EXISTS `rmp_response`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_response` (
  `rmp_id` bigint(20) DEFAULT NULL,
  `community_erp_yn` char(1) DEFAULT NULL,
  `facility_erp_yn` char(1) DEFAULT NULL,
  `erp_specific_yn` char(1) DEFAULT NULL,
  `erp_inform_yn` char(1) DEFAULT NULL,
  `erp_inform_hth_yn` char(1) DEFAULT NULL,
  `erp_review_date` varchar(25) DEFAULT NULL,
  `erp_training_date` varchar(25) DEFAULT NULL,
  `coord_agency` varchar(250) DEFAULT NULL,
  `coord_phone` varchar(10) DEFAULT NULL,
  `subto_osha191038` char(1) DEFAULT NULL,
  `subto_osha191020` char(1) DEFAULT NULL,
  `subto_cwa112` char(1) DEFAULT NULL,
  `subto_rcra264` char(1) DEFAULT NULL,
  `subto_opa90` char(1) DEFAULT NULL,
  `subto_state_epcra` char(1) DEFAULT NULL,
  `subto_other` varchar(200) DEFAULT NULL,
  UNIQUE KEY `rmpind_103` (`rmp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_scen_cd`
--

DROP TABLE IF EXISTS `rmp_scen_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_scen_cd` (
  `scen` char(1) DEFAULT NULL,
  `scen_tr` varchar(30) DEFAULT NULL,
  UNIQUE KEY `ind1` (`scen`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_submit_cd`
--

DROP TABLE IF EXISTS `rmp_submit_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_submit_cd` (
  `submit` char(3) DEFAULT NULL,
  `submit_tr` varchar(255) DEFAULT NULL,
  UNIQUE KEY `ind1` (`submit`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_topo_cd`
--

DROP TABLE IF EXISTS `rmp_topo_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_topo_cd` (
  `topo` char(1) DEFAULT NULL,
  `topo_tr` varchar(30) DEFAULT NULL,
  UNIQUE KEY `ind1` (`topo`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_wind_cd`
--

DROP TABLE IF EXISTS `rmp_wind_cd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_wind_cd` (
  `wind` char(1) DEFAULT NULL,
  `wind_tr` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_worst_flam`
--

DROP TABLE IF EXISTS `rmp_worst_flam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_worst_flam` (
  `flammable_id` int(11) DEFAULT NULL,
  `procchem_id` int(11) DEFAULT NULL,
  `analytical_basis` varchar(255) DEFAULT NULL,
  `quantity_lbs` double DEFAULT NULL,
  `endpoint_distance` float DEFAULT NULL,
  `population` varchar(9) DEFAULT NULL,
  `pr_schools` char(1) DEFAULT NULL,
  `pr_residences` char(1) DEFAULT NULL,
  `pr_hospitals` char(1) DEFAULT NULL,
  `pr_prisons` char(1) DEFAULT NULL,
  `pr_public_rec` char(1) DEFAULT NULL,
  `pr_comm_ind` char(1) DEFAULT NULL,
  `pr_othertype` varchar(200) DEFAULT NULL,
  `er_natlstateparks` char(1) DEFAULT NULL,
  `er_wildlife_sanct` char(1) DEFAULT NULL,
  `er_fedwilderness` char(1) DEFAULT NULL,
  `er_othertype` varchar(200) DEFAULT NULL,
  `pm_blastwalls` char(1) DEFAULT NULL,
  `pm_othertype` varchar(200) DEFAULT NULL,
  `ptrgraphic` varchar(12) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  UNIQUE KEY `rmpu03` (`flammable_id`),
  KEY `rmpj14` (`procchem_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `rmp_worst_tox`
--

DROP TABLE IF EXISTS `rmp_worst_tox`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmp_worst_tox` (
  `toxic_id` int(11) DEFAULT NULL,
  `procchem_id` int(11) DEFAULT NULL,
  `percent_weight` float DEFAULT NULL,
  `physical_state` char(1) DEFAULT NULL,
  `analytical_basis` varchar(255) DEFAULT NULL,
  `scenario` char(1) DEFAULT NULL,
  `quantity_lbs` double DEFAULT NULL,
  `release_duration` float DEFAULT NULL,
  `release_rate` float DEFAULT NULL,
  `wind_speed` float DEFAULT NULL,
  `stability_class` char(1) DEFAULT NULL,
  `topography` char(1) DEFAULT NULL,
  `endpoint_distance` float DEFAULT NULL,
  `population` varchar(9) DEFAULT NULL,
  `pr_schools` char(1) DEFAULT NULL,
  `pr_residences` char(1) DEFAULT NULL,
  `pr_hospitals` char(1) DEFAULT NULL,
  `pr_prisons` char(1) DEFAULT NULL,
  `pr_public_rec` char(1) DEFAULT NULL,
  `pr_comm_ind` char(1) DEFAULT NULL,
  `pr_othertype` varchar(200) DEFAULT NULL,
  `er_natlstateparks` char(1) DEFAULT NULL,
  `er_wildlifesanct` char(1) DEFAULT NULL,
  `er_fedwilderness` char(1) DEFAULT NULL,
  `er_othertype` varchar(200) DEFAULT NULL,
  `pm_dikes` char(1) DEFAULT NULL,
  `pm_enclosures` char(1) DEFAULT NULL,
  `pm_berms` char(1) DEFAULT NULL,
  `pm_drains` char(1) DEFAULT NULL,
  `pm_sumps` char(1) DEFAULT NULL,
  `pm_othertype` varchar(200) DEFAULT NULL,
  `ptrgraphic` varchar(12) DEFAULT NULL,
  `cbi_flag` char(1) DEFAULT NULL,
  UNIQUE KEY `rmpu01` (`toxic_id`),
  KEY `rmpj12` (`procchem_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
