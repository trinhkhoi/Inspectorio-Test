# Inspectorio-Test
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO inspectorio_acc;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO inspectorio_acc;

CREATE TABLE vendor(
   id SERIAL PRIMARY KEY NOT NULL,
   code CHAR(50),
   name TEXT,
   contacts VARCHAR(255)
);
CREATE TABLE factory(
   id SERIAL PRIMARY KEY NOT NULL,
   code CHAR(50),
   name TEXT,
   address VARCHAR(255),
   contacts VARCHAR(255)
);
CREATE TABLE general_info(
 id SERIAL PRIMARY KEY NOT NULL,
 vendor_id INT,
 factory_id INT,
 bmp_vendor CHAR(50),
 auditor VARCHAR(255),
 frm_level CHAR(10),
 date_created DATE
);
CREATE TABLE pom_info(
  id SERIAL PRIMARY KEY NOT NULL,
  general_id INT,
  vendor_pid CHAR(50),
  dpci CHAR(50),
  po_included CHAR(50),
  insp_type CHAR(10),
  po_qty INT,
  available_qty INT,
  description TEXT,
  is_pwi BOOLEAN
);
CREATE TABLE pif_info(
 id SERIAL PRIMARY KEY NOT NULL,
 general_id INT,
 vendor_pid CHAR(50),
 po_number CHAR(50),
 purpose VARCHAR(50),
 ship_begin_date DATE,
 ship_end_date DATE
);
CREATE TABLE item_info(
 id SERIAL PRIMARY KEY NOT NULL,
 general_id INT,
 item CHAR(50),
 item_description VARCHAR(255),
 po_number CHAR(50),
 order_qty INT,
 available_qty INT,
 vendor_pid CHAR(50),
 assortment_items CHAR(50)
);

CREATE TABLE sip_elements(
 id SERIAL PRIMARY KEY NOT NULL,
 general_id INT,
 vendor_pid CHAR(50),
 ppr_document BOOLEAN,
 red_seal BOOLEAN,
 technical_spec BOOLEAN,
 final_item_form BOOLEAN,
 total_program_quantity BOOLEAN,
 color_standard BOOLEAN,
 production_color BOOLEAN,
 trim_accessories BOOLEAN,
 yellow_seal BOOLEAN,
 product_testing_result BOOLEAN,
 floor_ready_requirement BOOLEAN,
 retail_packaging_design BOOLEAN,
 carton_mark BOOLEAN,
 factory_internal_report BOOLEAN,
 tcps_report BOOLEAN,
 completed_packing_list BOOLEAN
);