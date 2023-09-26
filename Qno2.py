# Write the program in any computer language to convert the floating decimal number
# to 14-bits binary floating-point model as the real digital values in the hardware
# memory. The example -26.62510 will be saved in the 14-bits hardware memory shown
# as follows
# def floating_model(floating_dec):
# """
# floating_model(-26.625)
# 1_10101_11010101
# """
# 1 1 0 1 0 1 1 1 0 1 0 1 0 1
# 1: negative
# 0: positive
# 510 (power of 2) +1610
# = 2110 = 101012
# 11010101 as significand
# 1 bit 5 bits 8 bits
# Total: 14 bits




def convert_binary(decimal):
    result = ""
    while decimal > 0:
        remainder = decimal % 2
        result = str(remainder) + result
        decimal //= 2
    return result


def floating_model(floating_dec):
    if floating_dec < 0:
        sign_bit = "1"
        floating_dec = abs(floating_dec)
    else:
        sign_bit = "0"

    exponent =  len(str(floating_dec))-1
    exponent_binary_initial =int(convert_binary(exponent + 16)[2:])
    exponent_binary = str(f"{exponent_binary_initial:05d}")
    
    initial_afterdec = str(floating_dec).split(".")[1]
    after_dec=float(str(f"0.{initial_afterdec}"))
    significand_binary=""
    for _ in range(8):
            after_dec *= 2
            bit = "1" if after_dec >= 1.0 else "0"
            significand_binary += bit
            after_dec -= int(after_dec)
    final_answe= str(convert_binary(int(floating_dec)))[2:]+significand_binary
    final_answer=final_answe[0:8]

    bit_14 = (sign_bit+"_"+ str(exponent_binary)+"_"+final_answer)
    return bit_14


floating_dec = float(input("Enter the number: "))
binary_floating_point = floating_model(floating_dec)
print(f"The 14 binary form is : {binary_floating_point}")