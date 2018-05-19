
class SipElement():
    def __init__(self, vendor_pid=None, ppr_document=None, red_seal=None, technical_spec=None, final_item_form=None,
                 total_program_quantity=None, color_standard=None, production_color=None, trim_accessories=None,
                 yellow_seal=None, product_testing_result=None, floor_ready_requirement=None, retail_packaging_design=None,
                 carton_mark=None, factory_internal_report=None, tcps_report=None, completed_packing_list=None):
        self.general_id = None
        self.vendor_pid = vendor_pid
        self.ppr_document = ppr_document
        self.red_seal = red_seal
        self.technical_spec = technical_spec
        self.final_item_form = final_item_form
        self.total_program_quantity = total_program_quantity
        self.color_standard = color_standard
        self.production_color =production_color
        self.trim_accessories = trim_accessories
        self.yellow_seal = yellow_seal
        self.product_testing_result = product_testing_result
        self.floor_ready_requirement = floor_ready_requirement
        self.retail_packaging_design = retail_packaging_design
        self.carton_mark = carton_mark
        self.factory_internal_report = factory_internal_report
        self.tcps_report = tcps_report
        self.completed_packing_list = completed_packing_list

    def get_data(self):
        return (self.general_id, self.vendor_pid, self.ppr_document, self.red_seal, self.technical_spec,
                self.final_item_form, self.total_program_quantity, self.color_standard, self.production_color,
                self.trim_accessories, self.yellow_seal, self.product_testing_result, self.floor_ready_requirement,
                self.retail_packaging_design, self.carton_mark, self.factory_internal_report, self.tcps_report,
                self.completed_packing_list)