class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        tmp = 10**9+7
        max_num_mod = (pow(2, p, tmp)-1)%tmp
        pair_product_mod = (max_num_mod-1)%tmp
        pair_cnt_mod_m_1 = (pow(2, p-1, tmp-1)-1) % (tmp-1)
        return (max_num_mod*pow(pair_product_mod, pair_cnt_mod_m_1, tmp)) % tmp
