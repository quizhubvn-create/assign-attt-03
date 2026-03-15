def get_degree(n):
    return n.bit_length() - 1

def gf2_divmod(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError()
    
    quotient = 0
    remainder = dividend
    divisor_deg = get_degree(divisor)
    
    while get_degree(remainder) >= divisor_deg:
        shift = get_degree(remainder) - divisor_deg
        quotient ^= (1 << shift)
        remainder ^= (divisor << shift)
    return quotient, remainder

def gf2_mul(a, b):
    res = 0
    for i in range(b.bit_length()):
        if (b >> i) & 1:
            res ^= (a << i)
    return res

def extended_gcd_gf2(a, m):
    old_r, r = m, a
    old_s, s = 0, 1
    
    print(f"{'Step':<5} | {'q':<10} | {'r':<10} | {'s':<10}")
    print("-" * 45)
    
    step = 0
    while r != 0:
        q, rem = gf2_divmod(old_r, r)
        
        # Cập nhật s: s = old_s ^ (q * s)
        new_s = old_s ^ gf2_mul(q, s)
        
        old_r, r = r, rem
        old_s, s = s, new_s
        
        print(f"{step:<5} | {q:<10} | {old_r:<10} | {old_s:<10}")
        step += 1
        
    return old_r, old_s

def main():
    MOD_POLY = 1033
    test_cases = [523, 1015]
    
    for a in test_cases:
        print(f"\nFinding inverse for a = {a}")
        gcd, inv = extended_gcd_gf2(a, MOD_POLY)
        print(f"Result: {a}^-1 = {inv}")
        
        # Kiểm tra lại: (a * inv) % MOD_POLY phải bằng 1
        check = gf2_divmod(gf2_mul(a, inv), MOD_POLY)[1]
        print(f"Verification (a * inv % m): {check}")

if __name__ == "__main__":
    main()