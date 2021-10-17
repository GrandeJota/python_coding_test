nums = eval("input(), "*4)
if ((nums[0] == '9' and (nums[-1] == '9' or nums[-1] == '8')) or (nums[0] == '8' and (nums[-1] == '9' or nums[-1] == '8'))) and (nums[1] == nums[2]):
    print("ignore")
else:
    print("answer")