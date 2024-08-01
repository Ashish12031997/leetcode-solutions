rh_users  = ["A", "B", "C"] #["A", "B", "C","A","D"]
new_users = ["B", "C", "D"]#["B", "C", "D","E","F"]

def top_referrers(rh_users, new_users):
    referrals = {}
    referral_set = set()
    # {A:3, B:2, C:1}
    
    for i in reversed(range(len(rh_users))):
        referrer = rh_users[i]
        referred = new_users[i]

        if referred not in referrals:
            referrals[referred] = 0
            if referrer not in referrals:
                referrals[referrer] = referrals[referred]+1
            else:
                referrals[referrer] = referrals[referred] + referrals[referrer] + 1
        else:
            if referrer not in referrals:
                referrals[referrer] = referrals[referred]+1
            else:
                referrals[referrer] = referrals[referred] + referrals[referrer] + 1
    x = sorted(referrals.items(), key = lambda x: (x[1]*-1, x[0]))
    return ["{} {}".format(k ,v) for k,v in x if v>0][:3]

        
top_3_referrers = top_referrers(rh_users, new_users)
print(top_3_referrers)
