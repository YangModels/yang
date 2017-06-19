import glob


class StatisticsInCatalog:
    def __init__(self):
        self.bbf_standard = glob.glob('./../../standard/bbf/standard' + '/*.yang')
        self.bbf_draft = glob.glob('./../../standard/bbf/draft' + '/*.yang')
        self.ieee_two_one_par = glob.glob('./../../standard/802.1' + '/*.yang')
        self.ieee_two_one_nopar = glob.glob('./../../experimental/802.1' + '/*.yang')
        self.ieee_two_three_par = glob.glob('./../../standard/802.3' + '/*.yang')
        self.ieee_two_three_nopar = glob.glob('./../../experimental/802.3' + '/*.yang')
        self.ieee_draft_par = glob.glob('./../../standard/draft' + '/*.yang')
        self.ietf_rfc = glob.glob('./../../standard/ietf/RFC' + '/*.yang')
        self.ietf_draft = glob.glob('./../../standard/ietf/DRAFT' + '/*.yang')
        self.openconfig = glob.glob('./../../experimental/openconfig' + '/*.yang')

        self.num_bbf_standard = 0
        self.num_bbf_draft = 0
        self.num_ieee_two_one_par = 0
        self.num_ieee_two_one_nopar = 0
        self.num_ieee_two_three_par = 0
        self.num_ieee_two_three_nopar = 0
        self.num_ieee_draft_par = 0
        self.num_ietf_rfc = 0
        self.num_ietf_draft = 0
        self.num_openconfig = 0
