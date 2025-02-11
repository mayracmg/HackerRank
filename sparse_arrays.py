from line_profiler import LineProfiler

strings = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf', 'na', 'asdjf', 'na', 'basdn', 'sdaklfj', 'asdjf']
queries = ['abcde', 'sdaklfj', 'asdjf', 'na', 'basdn']

#strings = ['yktkqhusnsbh', 'rzdgauiaqfd', 'qkhwynrlneksncv', 'fkgoemvsvg', 'eyrphlbrkw', 'mhakcihhthaajuamlg', 'hcbgcccvxs', 'outizmnucqkxdlfyxqg', 'palaxwkqxstdah', 'zktdtizkrcljederuxs', 'hvagmzgwgjmztncde', 'maenrdysbritmbtvyy', 'qacecpatcxoibelsaad', 'kbrkcxtvemurk', 'pcdvbycynxymmrajlh', 'vxkbsfyvywp', 'gpuvekxdscnfdferoax', 'ltlfgqpkuaw', 'auvffqnubmjhjsqqnwd', 'vnwwgxpvmnqev', 'xtujyxukoywdwu', 'rbydiynhywxgdfado', 'ghasjwxzvqjyiem', 'qmrsqbaatfzu', 'auvffqnubmjhjsqqnwd', 'veozzplakcamuplgpx', 'veozzplakcamuplgpx', 'azxxwcjitbkfkxabxv', 'cnzvvbicdocbfzcvg', 'znwxmwuzbzhgqoikovz', 'eaugxiwfddefirhcf', 'outizmnucqkxdlfyxqg', 'xungqrwaihorcwb', 'jsycwwqxrmpogurhbs', 'aizbsegmkcehkv', 'mhakcihhthaajuamlg', 'sjonqszwcwktxw', 'xfsjxooclcycwcn', 'cgxllhichirichbzma', 'cvyebywhzrheav', 'fswnwcgwwzazfbw', 'lywaxsogirghqgj', 'hlloonkdmanq', 'bjbedtpdcgcilwl', 'hqsdgjtpfxwzx', 'palaxwkqxstdah', 'uuqokimbilegfjrhzu', 'zfoofhbffi', 'llpntyizbeb', 'cnzvvbicdocbfzcvg', 'rbydiynhywxgdfado', 'pinxwmmeifueviczi', 'pcdvbycynxymmrajlh', 'tbsxdnjmagnpz', 'vgjxxhosif', 'ghasjwxzvqjyiem', 'vvufjbgdpvfy', 'llpntyizbeb', 'vgjxxhosif', 'bjbedtpdcgcilwl', 'hvagmzgwgjmztncde', 'hjnirpgylrvicvn', 'sjonqszwcwktxw', 'qacecpatcxoibelsaad', 'pcdvbycynxymmrajlh', 'dzstfixtnfccvwd', 'iglexamfdtvt', 'mhakcihhthaajuamlg', 'npjksoupvwuuklv', 'palaxwkqxstdah', 'pcdvbycynxymmrajlh', 'ghasjwxzvqjyiem', 'xfsjxooclcycwcn', 'uuqokimbilegfjrhzu', 'biviykdljlegtlimzil', 'zxyqmmiqnjnpg', 'sfduuipjzhhkvtiv', 'palaxwkqxstdah', 'kowvhbqhmthb', 'zfoofhbffi', 'sfduuipjzhhkvtiv', 'pinxwmmeifueviczi', 'mhakcihhthaajuamlg', 'aizbsegmkcehkv', 'xujqjgidmzuilic', 'iysxcgoufz', 'nitcfysgzvbcz', 'kbrkcxtvemurk', 'cvyebywhzrheav', 'hvagmzgwgjmztncde', 'hvagmzgwgjmztncde', 'qfvwoqfsoidz', 'vgjxxhosif', 'xfsjxooclcycwcn', 'dzstfixtnfccvwd', 'zktdtizkrcljederuxs', 'cvyebywhzrheav', 'hcbgcccvxs', 'bkclrgwnzmbut', 'xzscqzxmcejqjq', 'dvlahbxlvr', 'jsycwwqxrmpogurhbs', 'bypmwgpbgmsujnlowj', 'nddrscobfrojtwew', 'cnzvvbicdocbfzcvg', 'pinxwmmeifueviczi', 'auvffqnubmjhjsqqnwd', 'thzrjtjpousq', 'vpkytxfbeaqcioe', 'ejfeswctcdbrfnqy', 'pawsrhagbgzlsv', 'jsycwwqxrmpogurhbs', 'sgdpknswxysln', 'palaxwkqxstdah', 'sgdpknswxysln', 'ghasjwxzvqjyiem', 'hjnirpgylrvicvn', 'azxxwcjitbkfkxabxv', 'bkclrgwnzmbut', 'yjhejabudyfipd', 'ltlfgqpkuaw', 'aizbsegmkcehkv', 'palaxwkqxstdah', 'cvyebywhzrheav', 'skthxigeyrye', 'kbrkcxtvemurk', 'xfsjxooclcycwcn', 'vswlswwjpooelqttk', 'ltlfgqpkuaw', 'azxxwcjitbkfkxabxv', 'vfvvmfxhyenhzz', 'uuqokimbilegfjrhzu', 'jsycwwqxrmpogurhbs', 'vgjxxhosif', 'vxkbsfyvywp', 'hqsdgjtpfxwzx', 'zfoofhbffi', 'vpkytxfbeaqcioe', 'dvlahbxlvr', 'bypmwgpbgmsujnlowj', 'pinxwmmeifueviczi', 'hqsdgjtpfxwzx', 'hlloonkdmanq', 'iufqqsymxpsopnwuyh', 'xfsjxooclcycwcn', 'iufqqsymxpsopnwuyh', 'yjhejabudyfipd', 'npjksoupvwuuklv', 'tqfqorsmvuolskkvfj', 'xungqrwaihorcwb', 'wrxouegcmsfbhb', 'shrnzqokjsmtkcc', 'vswlswwjpooelqttk', 'xujqjgidmzuilic', 'cgxllhichirichbzma', 'tbsxdnjmagnpz', 'vpkytxfbeaqcioe', 'zrovgoudbnwrougxqz', 'qacecpatcxoibelsaad', 'bkclrgwnzmbut', 'hrwroqumokjcb', 'qkhwynrlneksncv', 'cmhggogvznkvwon', 'kbrkcxtvemurk', 'fkgoemvsvg', 'vnwwgxpvmnqev', 'bypmwgpbgmsujnlowj', 'skthxigeyrye', 'cmhggogvznkvwon', 'rzdgauiaqfd', 'sgdpknswxysln', 'pawsrhagbgzlsv', 'dgysbzweva', 'skthxigeyrye', 'skthxigeyrye', 'vgjxxhosif', 'vgjxxhosif', 'lywaxsogirghqgj', 'vvufjbgdpvfy', 'aizbsegmkcehkv', 'lfdfiuwfrnevaraz', 'iufqqsymxpsopnwuyh', 'yktkqhusnsbh', 'vpkytxfbeaqcioe', 'nddrscobfrojtwew', 'vvufjbgdpvfy', 'outizmnucqkxdlfyxqg', 'yjhejabudyfipd', 'vgjxxhosif', 'gdswuqisedicz', 'cnzvvbicdocbfzcvg', 'jsycwwqxrmpogurhbs', 'wrxouegcmsfbhb', 'uuqokimbilegfjrhzu', 'xujqjgidmzuilic', 'ltlfgqpkuaw', 'vnwwgxpvmnqev', 'fkgoemvsvg', 'xfsjxooclcycwcn', 'kowvhbqhmthb', 'gdswuqisedicz', 'uuqokimbilegfjrhzu', 'tbsxdnjmagnpz', 'veozzplakcamuplgpx', 'bypmwgpbgmsujnlowj', 'iufqqsymxpsopnwuyh', 'kbrkcxtvemurk', 'wrxouegcmsfbhb', 'vnwwgxpvmnqev', 'kowvhbqhmthb', 'tbsxdnjmagnpz', 'eyrphlbrkw', 'cgxllhichirichbzma', 'xujqjgidmzuilic', 'eyrphlbrkw', 'mhakcihhthaajuamlg', 'iufqqsymxpsopnwuyh', 'veozzplakcamuplgpx', 'lywaxsogirghqgj', 'lfdfiuwfrnevaraz', 'qfvwoqfsoidz', 'xujqjgidmzuilic', 'tbsxdnjmagnpz', 'cnzvvbicdocbfzcvg', 'pinxwmmeifueviczi', 'qacecpatcxoibelsaad', 'zktdtizkrcljederuxs', 'hqsdgjtpfxwzx', 'yktkqhusnsbh', 'ghasjwxzvqjyiem', 'fswnwcgwwzazfbw', 'znwxmwuzbzhgqoikovz', 'kowvhbqhmthb', 'kyqhtekrdfcigv', 'qfvwoqfsoidz', 'xtujyxukoywdwu', 'pinxwmmeifueviczi', 'bjbedtpdcgcilwl', 'zrovgoudbnwrougxqz', 'zfoofhbffi', 'cvyebywhzrheav', 'xzscqzxmcejqjq', 'fswnwcgwwzazfbw', 'eyrphlbrkw', 'wrxouegcmsfbhb', 'yjhejabudyfipd', 'rlmeprpzlifivjpdf', 'eyrphlbrkw', 'outizmnucqkxdlfyxqg', 'bypmwgpbgmsujnlowj', 'shrnzqokjsmtkcc', 'mhakcihhthaajuamlg', 'hcbgcccvxs', 'hvagmzgwgjmztncde', 'npjksoupvwuuklv', 'iysxcgoufz', 'vswlswwjpooelqttk', 'npjksoupvwuuklv', 'tbsxdnjmagnpz', 'npjksoupvwuuklv', 'dvlahbxlvr', 'zxyqmmiqnjnpg', 'vfvvmfxhyenhzz', 'qfvwoqfsoidz', 'biviykdljlegtlimzil', 'gfzkakdfwvflslyohzi', 'cmhggogvznkvwon', 'yktkqhusnsbh', 'eyrphlbrkw', 'llpntyizbeb', 'vgjxxhosif', 'shrnzqokjsmtkcc', 'ylwwujbuoxzxr', 'mobwckzanokv', 'kowvhbqhmthb', 'rzdgauiaqfd', 'vxkbsfyvywp', 'auvffqnubmjhjsqqnwd', 'outizmnucqkxdlfyxqg', 'elgnstionj', 'palaxwkqxstdah', 'nddrscobfrojtwew', 'shrnzqokjsmtkcc', 'vvufjbgdpvfy', 'sfduuipjzhhkvtiv', 'vswlswwjpooelqttk', 'dgysbzweva', 'hqsdgjtpfxwzx', 'vgjxxhosif', 'vfvvmfxhyenhzz', 'uhyatwgdcnwcxoas', 'llpntyizbeb', 'qmrsqbaatfzu', 'bkclrgwnzmbut', 'dvlahbxlvr', 'vswlswwjpooelqttk', 'rsffaewcsxxocl', 'hlloonkdmanq', 'veozzplakcamuplgpx', 'vxkbsfyvywp', 'qkhwynrlneksncv', 'mobwckzanokv', 'ghasjwxzvqjyiem', 'auvffqnubmjhjsqqnwd', 'biviykdljlegtlimzil', 'aizbsegmkcehkv', 'pinxwmmeifueviczi', 'sjonqszwcwktxw', 'kbrkcxtvemurk', 'xfsjxooclcycwcn', 'outizmnucqkxdlfyxqg', 'lywaxsogirghqgj', 'vfvvmfxhyenhzz', 'iglexamfdtvt', 'fkgoemvsvg', 'zfoofhbffi', 'palaxwkqxstdah', 'nitcfysgzvbcz', 'cmhggogvznkvwon', 'ejfeswctcdbrfnqy', 'sfduuipjzhhkvtiv', 'hlloonkdmanq', 'dgysbzweva', 'hlloonkdmanq', 'ghasjwxzvqjyiem', 'bjbedtpdcgcilwl', 'crexopedtp', 'iglexamfdtvt', 'gfzkakdfwvflslyohzi', 'bjbedtpdcgcilwl', 'uhyatwgdcnwcxoas', 'iysxcgoufz', 'znwxmwuzbzhgqoikovz', 'fkgoemvsvg', 'xtujyxukoywdwu', 'llpntyizbeb', 'xujqjgidmzuilic', 'vvufjbgdpvfy', 'gikbbcuucfceho', 'vxkbsfyvywp', 'npjksoupvwuuklv', 'nddrscobfrojtwew', 'gfzkakdfwvflslyohzi', 'gdswuqisedicz', 'ltlfgqpkuaw', 'sfduuipjzhhkvtiv', 'ltlfgqpkuaw', 'hlloonkdmanq', 'crexopedtp', 'pawsrhagbgzlsv', 'gpuvekxdscnfdferoax', 'vvufjbgdpvfy', 'rlmeprpzlifivjpdf', 'qfvwoqfsoidz', 'qkhwynrlneksncv', 'iysxcgoufz', 'kyqhtekrdfcigv', 'zfoofhbffi', 'zfoofhbffi', 'gikbbcuucfceho', 'vpkytxfbeaqcioe', 'mhakcihhthaajuamlg', 'npjksoupvwuuklv', 'cvyebywhzrheav', 'mhakcihhthaajuamlg', 'vvufjbgdpvfy', 'bjbedtpdcgcilwl', 'rbydiynhywxgdfado', 'sjonqszwcwktxw', 'xfsjxooclcycwcn', 'ejfeswctcdbrfnqy', 'azxxwcjitbkfkxabxv', 'rbydiynhywxgdfado', 'veozzplakcamuplgpx', 'shrnzqokjsmtkcc', 'ylwwujbuoxzxr', 'qfvwoqfsoidz', 'lcwvndudzxxoxzgti', 'aizbsegmkcehkv', 'shrnzqokjsmtkcc', 'elgnstionj', 'iglexamfdtvt', 'biviykdljlegtlimzil', 'maenrdysbritmbtvyy', 'cnzvvbicdocbfzcvg', 'rsffaewcsxxocl', 'vvufjbgdpvfy', 'eaugxiwfddefirhcf', 'lcwvndudzxxoxzgti', 'zrovgoudbnwrougxqz', 'bypmwgpbgmsujnlowj', 'kbrkcxtvemurk', 'qkhwynrlneksncv', 'ltlfgqpkuaw', 'llpntyizbeb', 'dgysbzweva', 'auvffqnubmjhjsqqnwd', 'vnwwgxpvmnqev', 'lcwvndudzxxoxzgti', 'hrwroqumokjcb', 'outizmnucqkxdlfyxqg', 'dvlahbxlvr', 'hrwroqumokjcb', 'qacecpatcxoibelsaad', 'zktdtizkrcljederuxs', 'yjhejabudyfipd', 'bypmwgpbgmsujnlowj', 'shrnzqokjsmtkcc', 'cvyebywhzrheav', 'uuqokimbilegfjrhzu', 'hqsdgjtpfxwzx', 'yjhejabudyfipd', 'ylwwujbuoxzxr', 'biviykdljlegtlimzil', 'hcbgcccvxs', 'hqsdgjtpfxwzx', 'rlmeprpzlifivjpdf', 'dzstfixtnfccvwd', 'tqfqorsmvuolskkvfj', 'jsycwwqxrmpogurhbs', 'vnwwgxpvmnqev', 'zktdtizkrcljederuxs', 'gikbbcuucfceho', 'dgysbzweva', 'cnzvvbicdocbfzcvg', 'hlloonkdmanq', 'ejfeswctcdbrfnqy', 'cnzvvbicdocbfzcvg', 'vpkytxfbeaqcioe', 'hqsdgjtpfxwzx', 'elgnstionj', 'znwxmwuzbzhgqoikovz', 'xtujyxukoywdwu', 'rzdgauiaqfd', 'uhyatwgdcnwcxoas', 'lcwvndudzxxoxzgti', 'qmrsqbaatfzu', 'vpkytxfbeaqcioe', 'eyrphlbrkw', 'dvlahbxlvr', 'ejfeswctcdbrfnqy', 'yktkqhusnsbh', 'gdswuqisedicz', 'jsycwwqxrmpogurhbs', 'eyrphlbrkw', 'iufqqsymxpsopnwuyh', 'hjnirpgylrvicvn', 'eyrphlbrkw', 'azxxwcjitbkfkxabxv', 'iglexamfdtvt', 'biviykdljlegtlimzil', 'nddrscobfrojtwew', 'ghasjwxzvqjyiem', 'lfdfiuwfrnevaraz', 'eaugxiwfddefirhcf', 'cgxllhichirichbzma', 'zfoofhbffi', 'bkclrgwnzmbut', 'zrovgoudbnwrougxqz', 'kowvhbqhmthb', 'hcbgcccvxs', 'uuqokimbilegfjrhzu', 'bypmwgpbgmsujnlowj', 'hjnirpgylrvicvn', 'vpkytxfbeaqcioe', 'veozzplakcamuplgpx', 'dvlahbxlvr', 'xfsjxooclcycwcn', 'eyrphlbrkw', 'gdswuqisedicz', 'eyrphlbrkw', 'ejfeswctcdbrfnqy', 'vpkytxfbeaqcioe', 'vfvvmfxhyenhzz', 'cmhggogvznkvwon', 'yktkqhusnsbh', 'eaugxiwfddefirhcf', 'kyqhtekrdfcigv', 'nitcfysgzvbcz', 'rlmeprpzlifivjpdf', 'vswlswwjpooelqttk', 'hrwroqumokjcb', 'hlloonkdmanq', 'kyqhtekrdfcigv', 'qmrsqbaatfzu', 'qacecpatcxoibelsaad', 'mhakcihhthaajuamlg', 'tqfqorsmvuolskkvfj', 'mhakcihhthaajuamlg', 'palaxwkqxstdah', 'dvlahbxlvr', 'xzscqzxmcejqjq', 'cgxllhichirichbzma', 'biviykdljlegtlimzil', 'wrxouegcmsfbhb', 'jsycwwqxrmpogurhbs', 'rnjifiaoeaweiqoxmsx', 'cvyebywhzrheav', 'qfvwoqfsoidz', 'veozzplakcamuplgpx', 'ghasjwxzvqjyiem', 'pawsrhagbgzlsv', 'lfdfiuwfrnevaraz', 'crexopedtp', 'auvffqnubmjhjsqqnwd', 'maenrdysbritmbtvyy', 'dvlahbxlvr', 'fswnwcgwwzazfbw', 'wgrpqtrvgixjpajoin', 'iglexamfdtvt', 'rnjifiaoeaweiqoxmsx', 'sfduuipjzhhkvtiv', 'pawsrhagbgzlsv', 'tqfqorsmvuolskkvfj', 'uuqokimbilegfjrhzu', 'bjbedtpdcgcilwl', 'hqsdgjtpfxwzx', 'zktdtizkrcljederuxs', 'skthxigeyrye', 'zrovgoudbnwrougxqz', 'npjksoupvwuuklv', 'maenrdysbritmbtvyy', 'zrovgoudbnwrougxqz', 'jsycwwqxrmpogurhbs', 'maenrdysbritmbtvyy', 'cmhggogvznkvwon', 'dgysbzweva', 'thzrjtjpousq', 'zfoofhbffi', 'qkhwynrlneksncv', 'qfvwoqfsoidz', 'lywaxsogirghqgj', 'xungqrwaihorcwb', 'hqsdgjtpfxwzx', 'hjnirpgylrvicvn', 'mhakcihhthaajuamlg', 'hjnirpgylrvicvn', 'sgdpknswxysln', 'qkhwynrlneksncv', 'nddrscobfrojtwew', 'jsycwwqxrmpogurhbs', 'lcwvndudzxxoxzgti', 'yjhejabudyfipd', 'lcwvndudzxxoxzgti', 'fkgoemvsvg', 'wrxouegcmsfbhb', 'mobwckzanokv', 'qmrsqbaatfzu', 'nitcfysgzvbcz', 'xfsjxooclcycwcn', 'elgnstionj', 'cgxllhichirichbzma', 'uhyatwgdcnwcxoas', 'nitcfysgzvbcz', 'eaugxiwfddefirhcf', 'kyqhtekrdfcigv', 'vxkbsfyvywp', 'crexopedtp', 'lcwvndudzxxoxzgti', 'yjhejabudyfipd', 'rlmeprpzlifivjpdf', 'tqfqorsmvuolskkvfj', 'cmhggogvznkvwon', 'qmrsqbaatfzu', 'gdswuqisedicz', 'rbydiynhywxgdfado', 'elgnstionj', 'qfvwoqfsoidz', 'cnzvvbicdocbfzcvg', 'gpuvekxdscnfdferoax', 'lfdfiuwfrnevaraz', 'dzstfixtnfccvwd', 'yjhejabudyfipd', 'aizbsegmkcehkv', 'iufqqsymxpsopnwuyh', 'dvlahbxlvr', 'znwxmwuzbzhgqoikovz', 'dvlahbxlvr', 'npjksoupvwuuklv', 'hvagmzgwgjmztncde', 'ghasjwxzvqjyiem', 'xtujyxukoywdwu', 'maenrdysbritmbtvyy', 'dgysbzweva', 'vgjxxhosif', 'hlloonkdmanq', 'zfoofhbffi', 'yjhejabudyfipd', 'thzrjtjpousq', 'kowvhbqhmthb', 'llpntyizbeb', 'outizmnucqkxdlfyxqg', 'vvufjbgdpvfy', 'shrnzqokjsmtkcc', 'sgdpknswxysln', 'cvyebywhzrheav', 'zfoofhbffi', 'vpkytxfbeaqcioe', 'iglexamfdtvt', 'yktkqhusnsbh', 'pinxwmmeifueviczi', 'ltlfgqpkuaw', 'jsycwwqxrmpogurhbs', 'sfduuipjzhhkvtiv', 'znwxmwuzbzhgqoikovz', 'hqsdgjtpfxwzx', 'vgjxxhosif', 'veozzplakcamuplgpx', 'outizmnucqkxdlfyxqg', 'znwxmwuzbzhgqoikovz', 'gfzkakdfwvflslyohzi', 'pawsrhagbgzlsv', 'pcdvbycynxymmrajlh', 'zxyqmmiqnjnpg', 'vpkytxfbeaqcioe', 'vxkbsfyvywp', 'kbrkcxtvemurk', 'pcdvbycynxymmrajlh', 'eyrphlbrkw', 'wrxouegcmsfbhb', 'kowvhbqhmthb', 'hlloonkdmanq', 'eyrphlbrkw', 'kbrkcxtvemurk', 'npjksoupvwuuklv', 'nitcfysgzvbcz', 'iysxcgoufz', 'dgysbzweva', 'skthxigeyrye', 'cvyebywhzrheav', 'zfoofhbffi', 'yktkqhusnsbh', 'uuqokimbilegfjrhzu', 'vfvvmfxhyenhzz', 'auvffqnubmjhjsqqnwd', 'zrovgoudbnwrougxqz', 'ghasjwxzvqjyiem', 'lywaxsogirghqgj', 'vfvvmfxhyenhzz', 'gpuvekxdscnfdferoax', 'pinxwmmeifueviczi', 'rsffaewcsxxocl', 'lywaxsogirghqgj', 'dgysbzweva', 'eaugxiwfddefirhcf', 'llpntyizbeb', 'cgxllhichirichbzma', 'eaugxiwfddefirhcf', 'uuqokimbilegfjrhzu', 'dzstfixtnfccvwd', 'vxkbsfyvywp', 'skthxigeyrye', 'sgdpknswxysln', 'llpntyizbeb', 'rnjifiaoeaweiqoxmsx', 'xzscqzxmcejqjq', 'uhyatwgdcnwcxoas', 'eaugxiwfddefirhcf', 'vvufjbgdpvfy', 'dvlahbxlvr', 'jsycwwqxrmpogurhbs', 'vswlswwjpooelqttk', 'fswnwcgwwzazfbw', 'hjnirpgylrvicvn', 'vswlswwjpooelqttk', 'mobwckzanokv', 'vgjxxhosif', 'sfduuipjzhhkvtiv', 'sgdpknswxysln', 'kbrkcxtvemurk', 'mobwckzanokv', 'veozzplakcamuplgpx', 'veozzplakcamuplgpx', 'outizmnucqkxdlfyxqg', 'yktkqhusnsbh', 'lywaxsogirghqgj', 'hvagmzgwgjmztncde', 'vxkbsfyvywp', 'bypmwgpbgmsujnlowj', 'iysxcgoufz', 'xzscqzxmcejqjq', 'eyrphlbrkw', 'iglexamfdtvt', 'cgxllhichirichbzma', 'iglexamfdtvt', 'cvyebywhzrheav', 'eaugxiwfddefirhcf', 'shrnzqokjsmtkcc', 'auvffqnubmjhjsqqnwd', 'lfdfiuwfrnevaraz', 'veozzplakcamuplgpx', 'gpuvekxdscnfdferoax', 'mhakcihhthaajuamlg', 'npjksoupvwuuklv', 'thzrjtjpousq', 'cnzvvbicdocbfzcvg', 'tbsxdnjmagnpz', 'maenrdysbritmbtvyy', 'zfoofhbffi', 'gfzkakdfwvflslyohzi', 'hlloonkdmanq', 'mhakcihhthaajuamlg', 'vxkbsfyvywp', 'biviykdljlegtlimzil', 'vnwwgxpvmnqev', 'qkhwynrlneksncv', 'ghasjwxzvqjyiem', 'wrxouegcmsfbhb', 'fkgoemvsvg', 'sfduuipjzhhkvtiv', 'iglexamfdtvt', 'llpntyizbeb', 'sjonqszwcwktxw', 'xujqjgidmzuilic', 'xungqrwaihorcwb', 'shrnzqokjsmtkcc', 'rlyqsifroactexlyzc', 'hvagmzgwgjmztncde', 'rnjifiaoeaweiqoxmsx', 'yktkqhusnsbh', 'xzscqzxmcejqjq', 'xfsjxooclcycwcn', 'bjbedtpdcgcilwl', 'npjksoupvwuuklv', 'qmrsqbaatfzu', 'xungqrwaihorcwb', 'lywaxsogirghqgj', 'sfduuipjzhhkvtiv', 'fswnwcgwwzazfbw', 'gfzkakdfwvflslyohzi', 'outizmnucqkxdlfyxqg', 'xzscqzxmcejqjq', 'tqfqorsmvuolskkvfj', 'dvlahbxlvr', 'ghasjwxzvqjyiem', 'ltlfgqpkuaw', 'hcbgcccvxs', 'rnjifiaoeaweiqoxmsx', 'cnzvvbicdocbfzcvg', 'qfvwoqfsoidz', 'outizmnucqkxdlfyxqg', 'yktkqhusnsbh', 'gfzkakdfwvflslyohzi', 'rnjifiaoeaweiqoxmsx', 'xfsjxooclcycwcn', 'mhakcihhthaajuamlg', 'maenrdysbritmbtvyy', 'zktdtizkrcljederuxs', 'xujqjgidmzuilic', 'aizbsegmkcehkv', 'rlyqsifroactexlyzc', 'hlloonkdmanq', 'nddrscobfrojtwew', 'vvufjbgdpvfy', 'sjonqszwcwktxw', 'sgdpknswxysln', 'crexopedtp', 'wgrpqtrvgixjpajoin', 'xtujyxukoywdwu', 'dvlahbxlvr', 'bkclrgwnzmbut', 'lfdfiuwfrnevaraz', 'dgysbzweva', 'kbrkcxtvemurk', 'ejfeswctcdbrfnqy', 'iglexamfdtvt', 'vxkbsfyvywp', 'kbrkcxtvemurk', 'rnjifiaoeaweiqoxmsx', 'wrxouegcmsfbhb', 'vfvvmfxhyenhzz', 'kyqhtekrdfcigv', 'maenrdysbritmbtvyy', 'biviykdljlegtlimzil', 'rlmeprpzlifivjpdf', 'zktdtizkrcljederuxs', 'xfsjxooclcycwcn', 'wgrpqtrvgixjpajoin', 'wgrpqtrvgixjpajoin', 'dvlahbxlvr', 'elgnstionj', 'palaxwkqxstdah', 'bkclrgwnzmbut', 'auvffqnubmjhjsqqnwd', 'fswnwcgwwzazfbw', 'eaugxiwfddefirhcf', 'pcdvbycynxymmrajlh', 'vgjxxhosif', 'uuqokimbilegfjrhzu', 'rzdgauiaqfd', 'ghasjwxzvqjyiem', 'vswlswwjpooelqttk', 'uhyatwgdcnwcxoas', 'vswlswwjpooelqttk', 'cnzvvbicdocbfzcvg', 'llpntyizbeb', 'zxyqmmiqnjnpg', 'skthxigeyrye', 'hrwroqumokjcb', 'nitcfysgzvbcz', 'dgysbzweva', 'fkgoemvsvg', 'vswlswwjpooelqttk', 'nitcfysgzvbcz', 'rzdgauiaqfd', 'bypmwgpbgmsujnlowj', 'vxkbsfyvywp', 'vvufjbgdpvfy', 'gfzkakdfwvflslyohzi', 'rsffaewcsxxocl', 'xtujyxukoywdwu', 'zrovgoudbnwrougxqz', 'pawsrhagbgzlsv', 'iglexamfdtvt', 'qacecpatcxoibelsaad', 'bjbedtpdcgcilwl', 'kyqhtekrdfcigv', 'hrwroqumokjcb', 'sfduuipjzhhkvtiv', 'iufqqsymxpsopnwuyh', 'lywaxsogirghqgj', 'rnjifiaoeaweiqoxmsx', 'vxkbsfyvywp', 'rsffaewcsxxocl', 'pcdvbycynxymmrajlh', 'lywaxsogirghqgj', 'dzstfixtnfccvwd', 'ghasjwxzvqjyiem', 'lcwvndudzxxoxzgti', 'sgdpknswxysln', 'azxxwcjitbkfkxabxv', 'tbsxdnjmagnpz', 'sjonqszwcwktxw', 'kowvhbqhmthb', 'zrovgoudbnwrougxqz', 'zktdtizkrcljederuxs', 'vpkytxfbeaqcioe', 'vfvvmfxhyenhzz', 'rzdgauiaqfd', 'zktdtizkrcljederuxs', 'wrxouegcmsfbhb', 'yjhejabudyfipd', 'qkhwynrlneksncv', 'wgrpqtrvgixjpajoin', 'vvufjbgdpvfy', 'kyqhtekrdfcigv', 'jsycwwqxrmpogurhbs', 'wgrpqtrvgixjpajoin', 'sgdpknswxysln', 'llpntyizbeb', 'biviykdljlegtlimzil', 'rnjifiaoeaweiqoxmsx', 'rbydiynhywxgdfado', 'hjnirpgylrvicvn', 'lcwvndudzxxoxzgti', 'vvufjbgdpvfy', 'eyrphlbrkw', 'uhyatwgdcnwcxoas', 'wrxouegcmsfbhb', 'hjnirpgylrvicvn', 'sgdpknswxysln', 'hvagmzgwgjmztncde', 'qacecpatcxoibelsaad', 'aizbsegmkcehkv', 'qacecpatcxoibelsaad', 'ylwwujbuoxzxr', 'hcbgcccvxs', 'fkgoemvsvg', 'xfsjxooclcycwcn', 'rlyqsifroactexlyzc', 'gfzkakdfwvflslyohzi', 'dgysbzweva', 'nddrscobfrojtwew', 'lcwvndudzxxoxzgti', 'npjksoupvwuuklv', 'sjonqszwcwktxw', 'kbrkcxtvemurk', 'qkhwynrlneksncv', 'auvffqnubmjhjsqqnwd', 'rlyqsifroactexlyzc', 'bkclrgwnzmbut', 'qmrsqbaatfzu', 'kbrkcxtvemurk', 'dgysbzweva', 'wgrpqtrvgixjpajoin', 'vpkytxfbeaqcioe', 'zfoofhbffi', 'vvufjbgdpvfy', 'nitcfysgzvbcz', 'xzscqzxmcejqjq', 'qmrsqbaatfzu', 'kowvhbqhmthb', 'lywaxsogirghqgj', 'hlloonkdmanq', 'ltlfgqpkuaw', 'jsycwwqxrmpogurhbs', 'cmhggogvznkvwon', 'vxkbsfyvywp', 'palaxwkqxstdah', 'vvufjbgdpvfy', 'gfzkakdfwvflslyohzi', 'qacecpatcxoibelsaad', 'lfdfiuwfrnevaraz', 'gdswuqisedicz', 'eyrphlbrkw', 'zfoofhbffi', 'uhyatwgdcnwcxoas', 'rbydiynhywxgdfado', 'dgysbzweva', 'auvffqnubmjhjsqqnwd', 'hcbgcccvxs', 'uhyatwgdcnwcxoas', 'sgdpknswxysln', 'xzscqzxmcejqjq', 'cmhggogvznkvwon', 'ghasjwxzvqjyiem', 'tqfqorsmvuolskkvfj', 'cvyebywhzrheav', 'tqfqorsmvuolskkvfj', 'xtujyxukoywdwu', 'dzstfixtnfccvwd', 'vgjxxhosif', 'biviykdljlegtlimzil', 'rlyqsifroactexlyzc', 'rlyqsifroactexlyzc', 'iysxcgoufz', 'bypmwgpbgmsujnlowj', 'biviykdljlegtlimzil', 'cgxllhichirichbzma', 'elgnstionj', 'rbydiynhywxgdfado', 'yktkqhusnsbh', 'hvagmzgwgjmztncde', 'sfduuipjzhhkvtiv', 'crexopedtp', 'eaugxiwfddefirhcf', 'hjnirpgylrvicvn', 'rzdgauiaqfd', 'mhakcihhthaajuamlg', 'zktdtizkrcljederuxs', 'vswlswwjpooelqttk', 'hqsdgjtpfxwzx', 'kyqhtekrdfcigv', 'llpntyizbeb', 'hqsdgjtpfxwzx', 'uhyatwgdcnwcxoas', 'dvlahbxlvr', 'dgysbzweva', 'maenrdysbritmbtvyy', 'crexopedtp', 'ltlfgqpkuaw', 'rlmeprpzlifivjpdf', 'zfoofhbffi', 'maenrdysbritmbtvyy', 'gfzkakdfwvflslyohzi', 'rbydiynhywxgdfado', 'jsycwwqxrmpogurhbs', 'mobwckzanokv', 'pcdvbycynxymmrajlh', 'npjksoupvwuuklv', 'zxyqmmiqnjnpg', 'dzstfixtnfccvwd', 'ejfeswctcdbrfnqy', 'rbydiynhywxgdfado', 'cvyebywhzrheav', 'vfvvmfxhyenhzz', 'kyqhtekrdfcigv', 'bypmwgpbgmsujnlowj', 'hcbgcccvxs', 'uuqokimbilegfjrhzu', 'fkgoemvsvg', 'npjksoupvwuuklv', 'eyrphlbrkw', 'sgdpknswxysln', 'mhakcihhthaajuamlg', 'vnwwgxpvmnqev', 'llpntyizbeb', 'zfoofhbffi', 'xfsjxooclcycwcn', 'kowvhbqhmthb']
#queries = ['xujqjgidmzuilic', 'qacecpatcxoibelsaad', 'hvagmzgwgjmztncde', 'vswlswwjpooelqttk', 'rbydiynhywxgdfado', 'rbydiynhywxgdfado', 'yktkqhusnsbh', 'qfvwoqfsoidz', 'vgjxxhosif', 'mobwckzanokv', 'bjbedtpdcgcilwl', 'azxxwcjitbkfkxabxv', 'wgrpqtrvgixjpajoin', 'thzrjtjpousq', 'jsycwwqxrmpogurhbs', 'xtujyxukoywdwu', 'rlmeprpzlifivjpdf', 'mhakcihhthaajuamlg', 'pcdvbycynxymmrajlh', 'pawsrhagbgzlsv', 'vfvvmfxhyenhzz', 'kbrkcxtvemurk', 'qfvwoqfsoidz', 'nddrscobfrojtwew', 'bjbedtpdcgcilwl', 'tbsxdnjmagnpz', 'zktdtizkrcljederuxs', 'nitcfysgzvbcz', 'dvlahbxlvr', 'xujqjgidmzuilic', 'fkgoemvsvg', 'jsycwwqxrmpogurhbs', 'nitcfysgzvbcz', 'dzstfixtnfccvwd', 'skthxigeyrye', 'vfvvmfxhyenhzz', 'eyrphlbrkw', 'gdswuqisedicz', 'gpuvekxdscnfdferoax', 'iufqqsymxpsopnwuyh', 'biviykdljlegtlimzil', 'azxxwcjitbkfkxabxv', 'lcwvndudzxxoxzgti', 'qfvwoqfsoidz', 'maenrdysbritmbtvyy', 'hjnirpgylrvicvn', 'yktkqhusnsbh', 'hlloonkdmanq', 'outizmnucqkxdlfyxqg', 'iysxcgoufz', 'tbsxdnjmagnpz', 'biviykdljlegtlimzil', 'yjhejabudyfipd', 'lywaxsogirghqgj', 'ejfeswctcdbrfnqy', 'vvufjbgdpvfy', 'bypmwgpbgmsujnlowj', 'xfsjxooclcycwcn', 'vgjxxhosif', 'fswnwcgwwzazfbw', 'veozzplakcamuplgpx', 'cnzvvbicdocbfzcvg', 'vfvvmfxhyenhzz', 'gdswuqisedicz', 'hrwroqumokjcb', 'elgnstionj', 'qfvwoqfsoidz', 'palaxwkqxstdah', 'gpuvekxdscnfdferoax', 'rsffaewcsxxocl', 'rbydiynhywxgdfado', 'vvufjbgdpvfy', 'elgnstionj', 'tbsxdnjmagnpz', 'bkclrgwnzmbut', 'nddrscobfrojtwew', 'gikbbcuucfceho', 'pcdvbycynxymmrajlh', 'bkclrgwnzmbut', 'xujqjgidmzuilic', 'hrwroqumokjcb', 'nitcfysgzvbcz', 'lcwvndudzxxoxzgti', 'rlyqsifroactexlyzc', 'iglexamfdtvt', 'qmrsqbaatfzu', 'hqsdgjtpfxwzx', 'bkclrgwnzmbut', 'rnjifiaoeaweiqoxmsx', 'iglexamfdtvt', 'rsffaewcsxxocl', 'sjonqszwcwktxw', 'maenrdysbritmbtvyy', 'kyqhtekrdfcigv', 'hrwroqumokjcb', 'vswlswwjpooelqttk', 'fswnwcgwwzazfbw', 'hvagmzgwgjmztncde', 'iufqqsymxpsopnwuyh', 'xzscqzxmcejqjq', 'vpkytxfbeaqcioe', 'qacecpatcxoibelsaad', 'llpntyizbeb', 'rsffaewcsxxocl', 'xtujyxukoywdwu', 'zfoofhbffi', 'skthxigeyrye', 'uuqokimbilegfjrhzu', 'xfsjxooclcycwcn', 'xzscqzxmcejqjq', 'outizmnucqkxdlfyxqg', 'qmrsqbaatfzu', 'zktdtizkrcljederuxs', 'bkclrgwnzmbut', 'pinxwmmeifueviczi', 'vfvvmfxhyenhzz', 'zxyqmmiqnjnpg', 'ghasjwxzvqjyiem', 'sjonqszwcwktxw', 'yjhejabudyfipd', 'rlyqsifroactexlyzc', 'wgrpqtrvgixjpajoin', 'zktdtizkrcljederuxs', 'cmhggogvznkvwon', 'cmhggogvznkvwon', 'pcdvbycynxymmrajlh', 'qacecpatcxoibelsaad', 'zxyqmmiqnjnpg', 'ylwwujbuoxzxr', 'cvyebywhzrheav', 'vswlswwjpooelqttk', 'rbydiynhywxgdfado', 'zfoofhbffi', 'cvyebywhzrheav', 'kowvhbqhmthb', 'mhakcihhthaajuamlg', 'vnwwgxpvmnqev', 'qmrsqbaatfzu', 'gpuvekxdscnfdferoax', 'vswlswwjpooelqttk', 'pinxwmmeifueviczi', 'rbydiynhywxgdfado', 'ylwwujbuoxzxr', 'uuqokimbilegfjrhzu', 'pinxwmmeifueviczi', 'xfsjxooclcycwcn', 'pcdvbycynxymmrajlh', 'fkgoemvsvg', 'vnwwgxpvmnqev', 'zktdtizkrcljederuxs', 'bkclrgwnzmbut', 'rsffaewcsxxocl', 'bjbedtpdcgcilwl', 'nitcfysgzvbcz', 'vxkbsfyvywp', 'rbydiynhywxgdfado', 'thzrjtjpousq', 'yktkqhusnsbh', 'elgnstionj', 'auvffqnubmjhjsqqnwd', 'npjksoupvwuuklv', 'dvlahbxlvr', 'bjbedtpdcgcilwl', 'gdswuqisedicz', 'gikbbcuucfceho', 'qfvwoqfsoidz', 'gikbbcuucfceho', 'rlmeprpzlifivjpdf', 'skthxigeyrye', 'shrnzqokjsmtkcc', 'veozzplakcamuplgpx', 'bkclrgwnzmbut', 'shrnzqokjsmtkcc', 'jsycwwqxrmpogurhbs', 'vnwwgxpvmnqev', 'kowvhbqhmthb', 'rsffaewcsxxocl', 'lfdfiuwfrnevaraz', 'yjhejabudyfipd', 'yjhejabudyfipd', 'rlyqsifroactexlyzc', 'veozzplakcamuplgpx', 'cnzvvbicdocbfzcvg', 'zxyqmmiqnjnpg', 'yjhejabudyfipd', 'yjhejabudyfipd', 'hqsdgjtpfxwzx', 'aizbsegmkcehkv', 'iysxcgoufz', 'hvagmzgwgjmztncde', 'iysxcgoufz', 'vvufjbgdpvfy', 'uuqokimbilegfjrhzu', 'veozzplakcamuplgpx', 'rsffaewcsxxocl', 'vnwwgxpvmnqev', 'kowvhbqhmthb', 'qmrsqbaatfzu', 'outizmnucqkxdlfyxqg', 'vswlswwjpooelqttk', 'rlyqsifroactexlyzc', 'veozzplakcamuplgpx', 'yktkqhusnsbh', 'mhakcihhthaajuamlg', 'wgrpqtrvgixjpajoin', 'fswnwcgwwzazfbw', 'qmrsqbaatfzu', 'zrovgoudbnwrougxqz', 'eyrphlbrkw', 'kowvhbqhmthb', 'rsffaewcsxxocl', 'zxyqmmiqnjnpg', 'bjbedtpdcgcilwl', 'uhyatwgdcnwcxoas', 'xtujyxukoywdwu', 'gdswuqisedicz', 'xfsjxooclcycwcn', 'sjonqszwcwktxw', 'aizbsegmkcehkv', 'crexopedtp', 'zrovgoudbnwrougxqz', 'rbydiynhywxgdfado', 'rnjifiaoeaweiqoxmsx', 'hcbgcccvxs', 'npjksoupvwuuklv', 'gdswuqisedicz', 'xungqrwaihorcwb', 'sfduuipjzhhkvtiv', 'vpkytxfbeaqcioe', 'uuqokimbilegfjrhzu', 'hjnirpgylrvicvn', 'maenrdysbritmbtvyy', 'qmrsqbaatfzu', 'kowvhbqhmthb', 'nddrscobfrojtwew', 'tqfqorsmvuolskkvfj', 'ylwwujbuoxzxr', 'iysxcgoufz', 'jsycwwqxrmpogurhbs', 'sjonqszwcwktxw', 'vfvvmfxhyenhzz', 'mobwckzanokv', 'rlyqsifroactexlyzc', 'iglexamfdtvt', 'maenrdysbritmbtvyy', 'wrxouegcmsfbhb', 'pinxwmmeifueviczi', 'npjksoupvwuuklv', 'rzdgauiaqfd', 'zxyqmmiqnjnpg', 'qkhwynrlneksncv', 'veozzplakcamuplgpx', 'xungqrwaihorcwb', 'lywaxsogirghqgj', 'kowvhbqhmthb', 'llpntyizbeb', 'xtujyxukoywdwu', 'ejfeswctcdbrfnqy', 'hjnirpgylrvicvn', 'npjksoupvwuuklv', 'vnwwgxpvmnqev', 'dzstfixtnfccvwd', 'azxxwcjitbkfkxabxv', 'jsycwwqxrmpogurhbs', 'xujqjgidmzuilic', 'vgjxxhosif', 'rzdgauiaqfd', 'hlloonkdmanq', 'kbrkcxtvemurk', 'auvffqnubmjhjsqqnwd', 'aizbsegmkcehkv', 'gfzkakdfwvflslyohzi', 'hqsdgjtpfxwzx', 'mobwckzanokv', 'qmrsqbaatfzu', 'hjnirpgylrvicvn', 'zxyqmmiqnjnpg', 'pawsrhagbgzlsv', 'kowvhbqhmthb', 'zxyqmmiqnjnpg', 'dvlahbxlvr', 'dgysbzweva', 'auvffqnubmjhjsqqnwd', 'crexopedtp', 'vgjxxhosif', 'kyqhtekrdfcigv', 'vxkbsfyvywp', 'gfzkakdfwvflslyohzi', 'kbrkcxtvemurk', 'biviykdljlegtlimzil', 'fkgoemvsvg', 'outizmnucqkxdlfyxqg', 'ltlfgqpkuaw', 'hcbgcccvxs', 'xzscqzxmcejqjq', 'rnjifiaoeaweiqoxmsx', 'zrovgoudbnwrougxqz', 'sfduuipjzhhkvtiv', 'qmrsqbaatfzu', 'lcwvndudzxxoxzgti', 'rnjifiaoeaweiqoxmsx', 'vxkbsfyvywp', 'uhyatwgdcnwcxoas', 'eyrphlbrkw', 'gpuvekxdscnfdferoax', 'rzdgauiaqfd', 'cgxllhichirichbzma', 'bypmwgpbgmsujnlowj', 'hjnirpgylrvicvn', 'hvagmzgwgjmztncde', 'qmrsqbaatfzu', 'pcdvbycynxymmrajlh', 'rzdgauiaqfd', 'vvufjbgdpvfy', 'fkgoemvsvg', 'vxkbsfyvywp', 'maenrdysbritmbtvyy', 'rsffaewcsxxocl', 'hlloonkdmanq', 'tqfqorsmvuolskkvfj', 'kowvhbqhmthb', 'hlloonkdmanq', 'gdswuqisedicz', 'npjksoupvwuuklv', 'pcdvbycynxymmrajlh', 'vxkbsfyvywp', 'rnjifiaoeaweiqoxmsx', 'rlmeprpzlifivjpdf', 'azxxwcjitbkfkxabxv', 'rsffaewcsxxocl', 'ejfeswctcdbrfnqy', 'xzscqzxmcejqjq', 'thzrjtjpousq', 'crexopedtp', 'gfzkakdfwvflslyohzi', 'lfdfiuwfrnevaraz', 'hrwroqumokjcb', 'rlyqsifroactexlyzc', 'lfdfiuwfrnevaraz', 'auvffqnubmjhjsqqnwd', 'ghasjwxzvqjyiem', 'pinxwmmeifueviczi', 'skthxigeyrye', 'fswnwcgwwzazfbw', 'bjbedtpdcgcilwl', 'npjksoupvwuuklv', 'qacecpatcxoibelsaad', 'pinxwmmeifueviczi', 'vfvvmfxhyenhzz', 'qfvwoqfsoidz', 'iglexamfdtvt', 'fswnwcgwwzazfbw', 'eaugxiwfddefirhcf', 'veozzplakcamuplgpx', 'cgxllhichirichbzma', 'pinxwmmeifueviczi', 'uhyatwgdcnwcxoas', 'bypmwgpbgmsujnlowj', 'vswlswwjpooelqttk', 'biviykdljlegtlimzil', 'rzdgauiaqfd', 'xungqrwaihorcwb', 'cvyebywhzrheav', 'qkhwynrlneksncv', 'cmhggogvznkvwon', 'llpntyizbeb', 'ghasjwxzvqjyiem', 'wgrpqtrvgixjpajoin', 'vgjxxhosif', 'zrovgoudbnwrougxqz', 'vnwwgxpvmnqev', 'cnzvvbicdocbfzcvg', 'vpkytxfbeaqcioe', 'gdswuqisedicz', 'llpntyizbeb', 'rbydiynhywxgdfado', 'rbydiynhywxgdfado', 'sfduuipjzhhkvtiv', 'mhakcihhthaajuamlg', 'zfoofhbffi', 'dvlahbxlvr', 'kbrkcxtvemurk', 'hcbgcccvxs', 'eyrphlbrkw', 'hvagmzgwgjmztncde', 'rbydiynhywxgdfado', 'hvagmzgwgjmztncde', 'ltlfgqpkuaw', 'fswnwcgwwzazfbw', 'ghasjwxzvqjyiem', 'rnjifiaoeaweiqoxmsx', 'lfdfiuwfrnevaraz', 'ylwwujbuoxzxr', 'crexopedtp', 'palaxwkqxstdah', 'hjnirpgylrvicvn', 'hcbgcccvxs', 'bkclrgwnzmbut', 'znwxmwuzbzhgqoikovz', 'crexopedtp', 'mobwckzanokv', 'iufqqsymxpsopnwuyh', 'hlloonkdmanq', 'lcwvndudzxxoxzgti', 'yjhejabudyfipd', 'npjksoupvwuuklv', 'biviykdljlegtlimzil', 'vpkytxfbeaqcioe', 'npjksoupvwuuklv', 'tbsxdnjmagnpz', 'tqfqorsmvuolskkvfj', 'dgysbzweva', 'azxxwcjitbkfkxabxv', 'yktkqhusnsbh', 'wrxouegcmsfbhb', 'fkgoemvsvg', 'yjhejabudyfipd', 'azxxwcjitbkfkxabxv', 'hvagmzgwgjmztncde', 'vswlswwjpooelqttk', 'yjhejabudyfipd', 'uhyatwgdcnwcxoas', 'vnwwgxpvmnqev', 'npjksoupvwuuklv', 'eyrphlbrkw', 'ghasjwxzvqjyiem', 'kbrkcxtvemurk', 'znwxmwuzbzhgqoikovz', 'hvagmzgwgjmztncde', 'qfvwoqfsoidz', 'lfdfiuwfrnevaraz', 'skthxigeyrye', 'hjnirpgylrvicvn', 'gdswuqisedicz', 'vgjxxhosif', 'tbsxdnjmagnpz', 'lfdfiuwfrnevaraz', 'jsycwwqxrmpogurhbs', 'hvagmzgwgjmztncde', 'auvffqnubmjhjsqqnwd', 'sgdpknswxysln', 'cgxllhichirichbzma', 'kbrkcxtvemurk', 'hrwroqumokjcb', 'gikbbcuucfceho', 'zxyqmmiqnjnpg', 'xfsjxooclcycwcn', 'hqsdgjtpfxwzx', 'eaugxiwfddefirhcf', 'tqfqorsmvuolskkvfj', 'dzstfixtnfccvwd', 'vswlswwjpooelqttk', 'bypmwgpbgmsujnlowj', 'cvyebywhzrheav', 'qkhwynrlneksncv', 'gpuvekxdscnfdferoax', 'ylwwujbuoxzxr', 'rnjifiaoeaweiqoxmsx', 'pcdvbycynxymmrajlh', 'qfvwoqfsoidz', 'yktkqhusnsbh', 'hvagmzgwgjmztncde', 'auvffqnubmjhjsqqnwd', 'kbrkcxtvemurk', 'bjbedtpdcgcilwl', 'pinxwmmeifueviczi', 'vvufjbgdpvfy', 'zfoofhbffi', 'zxyqmmiqnjnpg', 'vswlswwjpooelqttk', 'rzdgauiaqfd', 'xfsjxooclcycwcn', 'skthxigeyrye', 'rzdgauiaqfd', 'qmrsqbaatfzu', 'auvffqnubmjhjsqqnwd', 'hqsdgjtpfxwzx', 'gikbbcuucfceho', 'auvffqnubmjhjsqqnwd', 'kyqhtekrdfcigv', 'qfvwoqfsoidz', 'hvagmzgwgjmztncde', 'hjnirpgylrvicvn', 'outizmnucqkxdlfyxqg', 'qmrsqbaatfzu', 'pcdvbycynxymmrajlh', 'znwxmwuzbzhgqoikovz', 'jsycwwqxrmpogurhbs', 'hcbgcccvxs', 'azxxwcjitbkfkxabxv', 'biviykdljlegtlimzil', 'gfzkakdfwvflslyohzi', 'tqfqorsmvuolskkvfj', 'sgdpknswxysln', 'veozzplakcamuplgpx', 'rzdgauiaqfd', 'hlloonkdmanq', 'znwxmwuzbzhgqoikovz', 'hjnirpgylrvicvn', 'zrovgoudbnwrougxqz', 'yjhejabudyfipd', 'veozzplakcamuplgpx', 'lcwvndudzxxoxzgti', 'shrnzqokjsmtkcc', 'xujqjgidmzuilic', 'gikbbcuucfceho', 'kbrkcxtvemurk', 'zktdtizkrcljederuxs', 'uhyatwgdcnwcxoas', 'vnwwgxpvmnqev', 'cmhggogvznkvwon', 'cnzvvbicdocbfzcvg', 'vswlswwjpooelqttk', 'skthxigeyrye', 'xtujyxukoywdwu', 'rlyqsifroactexlyzc', 'hqsdgjtpfxwzx', 'ltlfgqpkuaw', 'xujqjgidmzuilic', 'nitcfysgzvbcz', 'palaxwkqxstdah', 'cvyebywhzrheav', 'jsycwwqxrmpogurhbs', 'aizbsegmkcehkv', 'dvlahbxlvr', 'mhakcihhthaajuamlg', 'hcbgcccvxs', 'shrnzqokjsmtkcc', 'yjhejabudyfipd', 'pawsrhagbgzlsv', 'znwxmwuzbzhgqoikovz', 'llpntyizbeb', 'bypmwgpbgmsujnlowj', 'uuqokimbilegfjrhzu', 'ylwwujbuoxzxr', 'gdswuqisedicz', 'hcbgcccvxs', 'qmrsqbaatfzu', 'veozzplakcamuplgpx', 'vxkbsfyvywp', 'tbsxdnjmagnpz', 'mobwckzanokv', 'rlyqsifroactexlyzc', 'zxyqmmiqnjnpg', 'pawsrhagbgzlsv', 'auvffqnubmjhjsqqnwd', 'wgrpqtrvgixjpajoin', 'gpuvekxdscnfdferoax', 'qmrsqbaatfzu', 'skthxigeyrye', 'lywaxsogirghqgj', 'mhakcihhthaajuamlg', 'outizmnucqkxdlfyxqg', 'bjbedtpdcgcilwl', 'vnwwgxpvmnqev', 'hqsdgjtpfxwzx', 'gfzkakdfwvflslyohzi', 'kyqhtekrdfcigv', 'eyrphlbrkw', 'rlmeprpzlifivjpdf', 'mobwckzanokv', 'hvagmzgwgjmztncde', 'bjbedtpdcgcilwl', 'hcbgcccvxs', 'bypmwgpbgmsujnlowj', 'lcwvndudzxxoxzgti', 'sfduuipjzhhkvtiv', 'cmhggogvznkvwon', 'qacecpatcxoibelsaad', 'tqfqorsmvuolskkvfj', 'bjbedtpdcgcilwl', 'lywaxsogirghqgj', 'kowvhbqhmthb', 'ylwwujbuoxzxr', 'cgxllhichirichbzma', 'maenrdysbritmbtvyy', 'outizmnucqkxdlfyxqg', 'nitcfysgzvbcz', 'hvagmzgwgjmztncde', 'sgdpknswxysln', 'wgrpqtrvgixjpajoin', 'lywaxsogirghqgj', 'dgysbzweva', 'hcbgcccvxs', 'cmhggogvznkvwon', 'gdswuqisedicz', 'zrovgoudbnwrougxqz', 'vpkytxfbeaqcioe', 'gdswuqisedicz', 'zrovgoudbnwrougxqz', 'crexopedtp', 'mobwckzanokv', 'zfoofhbffi', 'hcbgcccvxs', 'rlyqsifroactexlyzc', 'ltlfgqpkuaw', 'ylwwujbuoxzxr', 'gikbbcuucfceho', 'cgxllhichirichbzma', 'gdswuqisedicz', 'vswlswwjpooelqttk', 'lfdfiuwfrnevaraz', 'sjonqszwcwktxw', 'yjhejabudyfipd', 'vswlswwjpooelqttk', 'rnjifiaoeaweiqoxmsx', 'cmhggogvznkvwon', 'fkgoemvsvg', 'hvagmzgwgjmztncde', 'cgxllhichirichbzma', 'iufqqsymxpsopnwuyh', 'iysxcgoufz', 'auvffqnubmjhjsqqnwd', 'wgrpqtrvgixjpajoin', 'ltlfgqpkuaw', 'palaxwkqxstdah', 'vxkbsfyvywp', 'iufqqsymxpsopnwuyh', 'vswlswwjpooelqttk', 'npjksoupvwuuklv', 'skthxigeyrye', 'ltlfgqpkuaw', 'znwxmwuzbzhgqoikovz', 'dgysbzweva', 'nitcfysgzvbcz', 'vswlswwjpooelqttk', 'hvagmzgwgjmztncde', 'wgrpqtrvgixjpajoin', 'gdswuqisedicz', 'iysxcgoufz', 'llpntyizbeb', 'gikbbcuucfceho', 'npjksoupvwuuklv', 'kbrkcxtvemurk', 'tqfqorsmvuolskkvfj', 'auvffqnubmjhjsqqnwd', 'yjhejabudyfipd', 'kowvhbqhmthb', 'xtujyxukoywdwu', 'qfvwoqfsoidz', 'qfvwoqfsoidz', 'vswlswwjpooelqttk', 'hvagmzgwgjmztncde', 'nitcfysgzvbcz', 'yjhejabudyfipd', 'vnwwgxpvmnqev', 'ylwwujbuoxzxr', 'veozzplakcamuplgpx', 'qfvwoqfsoidz', 'lfdfiuwfrnevaraz', 'mobwckzanokv', 'rbydiynhywxgdfado', 'iglexamfdtvt', 'rnjifiaoeaweiqoxmsx', 'zfoofhbffi', 'cvyebywhzrheav', 'eyrphlbrkw', 'elgnstionj', 'npjksoupvwuuklv', 'iysxcgoufz', 'eaugxiwfddefirhcf', 'palaxwkqxstdah', 'zktdtizkrcljederuxs', 'palaxwkqxstdah', 'dgysbzweva', 'hlloonkdmanq', 'gdswuqisedicz', 'outizmnucqkxdlfyxqg', 'llpntyizbeb', 'vgjxxhosif', 'skthxigeyrye', 'lfdfiuwfrnevaraz', 'dgysbzweva', 'vnwwgxpvmnqev', 'nddrscobfrojtwew', 'zxyqmmiqnjnpg', 'ltlfgqpkuaw', 'lywaxsogirghqgj', 'llpntyizbeb', 'wgrpqtrvgixjpajoin', 'azxxwcjitbkfkxabxv', 'ltlfgqpkuaw', 'maenrdysbritmbtvyy', 'llpntyizbeb', 'mhakcihhthaajuamlg', 'thzrjtjpousq', 'znwxmwuzbzhgqoikovz', 'bypmwgpbgmsujnlowj', 'rlmeprpzlifivjpdf', 'hlloonkdmanq', 'xujqjgidmzuilic', 'vgjxxhosif', 'vfvvmfxhyenhzz', 'eaugxiwfddefirhcf', 'ejfeswctcdbrfnqy', 'thzrjtjpousq', 'dzstfixtnfccvwd', 'vswlswwjpooelqttk', 'fswnwcgwwzazfbw', 'gfzkakdfwvflslyohzi', 'xungqrwaihorcwb', 'rnjifiaoeaweiqoxmsx', 'bjbedtpdcgcilwl', 'hjnirpgylrvicvn', 'kyqhtekrdfcigv', 'pawsrhagbgzlsv', 'xujqjgidmzuilic', 'kowvhbqhmthb', 'ltlfgqpkuaw', 'fswnwcgwwzazfbw', 'lcwvndudzxxoxzgti', 'vxkbsfyvywp', 'nitcfysgzvbcz', 'fkgoemvsvg', 'wgrpqtrvgixjpajoin', 'cvyebywhzrheav', 'eaugxiwfddefirhcf', 'shrnzqokjsmtkcc', 'sgdpknswxysln', 'cnzvvbicdocbfzcvg', 'shrnzqokjsmtkcc', 'xtujyxukoywdwu', 'rlyqsifroactexlyzc', 'hlloonkdmanq', 'bkclrgwnzmbut', 'zxyqmmiqnjnpg', 'skthxigeyrye', 'ltlfgqpkuaw', 'hjnirpgylrvicvn', 'wrxouegcmsfbhb', 'maenrdysbritmbtvyy', 'ejfeswctcdbrfnqy', 'kbrkcxtvemurk', 'rlmeprpzlifivjpdf', 'pawsrhagbgzlsv', 'rlyqsifroactexlyzc', 'biviykdljlegtlimzil', 'ghasjwxzvqjyiem', 'xzscqzxmcejqjq', 'pcdvbycynxymmrajlh', 'rsffaewcsxxocl', 'rsffaewcsxxocl', 'sfduuipjzhhkvtiv', 'xfsjxooclcycwcn', 'qmrsqbaatfzu', 'sjonqszwcwktxw', 'iglexamfdtvt', 'vnwwgxpvmnqev', 'mobwckzanokv', 'skthxigeyrye', 'vfvvmfxhyenhzz', 'yjhejabudyfipd', 'jsycwwqxrmpogurhbs', 'hjnirpgylrvicvn', 'kowvhbqhmthb', 'outizmnucqkxdlfyxqg', 'gdswuqisedicz', 'vgjxxhosif', 'rlmeprpzlifivjpdf', 'nddrscobfrojtwew', 'ltlfgqpkuaw', 'palaxwkqxstdah', 'hcbgcccvxs', 'gfzkakdfwvflslyohzi', 'biviykdljlegtlimzil', 'gpuvekxdscnfdferoax', 'palaxwkqxstdah', 'xzscqzxmcejqjq', 'gdswuqisedicz', 'zfoofhbffi', 'lywaxsogirghqgj', 'iglexamfdtvt', 'mhakcihhthaajuamlg', 'dvlahbxlvr', 'npjksoupvwuuklv', 'sgdpknswxysln', 'qfvwoqfsoidz', 'xfsjxooclcycwcn', 'yjhejabudyfipd', 'hqsdgjtpfxwzx', 'azxxwcjitbkfkxabxv', 'hlloonkdmanq', 'fkgoemvsvg', 'kbrkcxtvemurk', 'hqsdgjtpfxwzx', 'fswnwcgwwzazfbw', 'kbrkcxtvemurk', 'elgnstionj', 'nddrscobfrojtwew', 'biviykdljlegtlimzil', 'palaxwkqxstdah', 'xfsjxooclcycwcn', 'pawsrhagbgzlsv', 'vfvvmfxhyenhzz', 'vpkytxfbeaqcioe', 'aizbsegmkcehkv', 'sjonqszwcwktxw', 'gikbbcuucfceho', 'ghasjwxzvqjyiem', 'lywaxsogirghqgj', 'hlloonkdmanq', 'hlloonkdmanq', 'vgjxxhosif', 'xzscqzxmcejqjq', 'qfvwoqfsoidz', 'iysxcgoufz', 'vpkytxfbeaqcioe', 'rlmeprpzlifivjpdf', 'gikbbcuucfceho', 'elgnstionj', 'rbydiynhywxgdfado', 'hjnirpgylrvicvn', 'wrxouegcmsfbhb', 'iufqqsymxpsopnwuyh', 'dvlahbxlvr', 'gfzkakdfwvflslyohzi', 'gfzkakdfwvflslyohzi', 'sjonqszwcwktxw', 'gfzkakdfwvflslyohzi', 'lywaxsogirghqgj', 'xujqjgidmzuilic', 'rsffaewcsxxocl', 'wgrpqtrvgixjpajoin', 'maenrdysbritmbtvyy', 'lcwvndudzxxoxzgti', 'hcbgcccvxs', 'iysxcgoufz', 'vgjxxhosif', 'maenrdysbritmbtvyy', 'eaugxiwfddefirhcf', 'zxyqmmiqnjnpg', 'sfduuipjzhhkvtiv', 'yjhejabudyfipd', 'ghasjwxzvqjyiem', 'kyqhtekrdfcigv', 'cvyebywhzrheav', 'crexopedtp', 'zktdtizkrcljederuxs', 'gfzkakdfwvflslyohzi', 'ejfeswctcdbrfnqy', 'kyqhtekrdfcigv', 'hcbgcccvxs', 'hrwroqumokjcb', 'zxyqmmiqnjnpg', 'vswlswwjpooelqttk', 'cvyebywhzrheav', 'shrnzqokjsmtkcc', 'yktkqhusnsbh', 'eaugxiwfddefirhcf', 'rlmeprpzlifivjpdf', 'dvlahbxlvr', 'ghasjwxzvqjyiem', 'zxyqmmiqnjnpg', 'azxxwcjitbkfkxabxv', 'gpuvekxdscnfdferoax', 'cmhggogvznkvwon', 'sjonqszwcwktxw', 'thzrjtjpousq', 'pawsrhagbgzlsv', 'hvagmzgwgjmztncde', 'uhyatwgdcnwcxoas', 'fkgoemvsvg', 'xfsjxooclcycwcn', 'vfvvmfxhyenhzz', 'hjnirpgylrvicvn', 'vfvvmfxhyenhzz', 'sjonqszwcwktxw', 'iysxcgoufz', 'palaxwkqxstdah', 'palaxwkqxstdah', 'iufqqsymxpsopnwuyh', 'llpntyizbeb', 'qacecpatcxoibelsaad', 'bypmwgpbgmsujnlowj', 'dvlahbxlvr', 'xzscqzxmcejqjq', 'sjonqszwcwktxw', 'aizbsegmkcehkv', 'vswlswwjpooelqttk', 'hqsdgjtpfxwzx', 'ejfeswctcdbrfnqy', 'xungqrwaihorcwb', 'qkhwynrlneksncv', 'xfsjxooclcycwcn', 'rsffaewcsxxocl', 'nitcfysgzvbcz', 'vgjxxhosif', 'xungqrwaihorcwb', 'eaugxiwfddefirhcf', 'outizmnucqkxdlfyxqg', 'uhyatwgdcnwcxoas', 'pinxwmmeifueviczi', 'auvffqnubmjhjsqqnwd', 'rbydiynhywxgdfado', 'gfzkakdfwvflslyohzi', 'wrxouegcmsfbhb', 'rsffaewcsxxocl', 'vgjxxhosif', 'llpntyizbeb', 'bkclrgwnzmbut', 'mhakcihhthaajuamlg', 'zfoofhbffi', 'aizbsegmkcehkv', 'xfsjxooclcycwcn', 'ltlfgqpkuaw', 'zrovgoudbnwrougxqz', 'pawsrhagbgzlsv', 'rbydiynhywxgdfado', 'zktdtizkrcljederuxs', 'nitcfysgzvbcz', 'vvufjbgdpvfy', 'uhyatwgdcnwcxoas', 'shrnzqokjsmtkcc', 'mhakcihhthaajuamlg', 'mhakcihhthaajuamlg', 'uhyatwgdcnwcxoas', 'vxkbsfyvywp', 'gdswuqisedicz', 'eyrphlbrkw', 'dgysbzweva', 'tqfqorsmvuolskkvfj', 'vgjxxhosif', 'xungqrwaihorcwb', 'mhakcihhthaajuamlg', 'zrovgoudbnwrougxqz', 'bypmwgpbgmsujnlowj', 'vgjxxhosif', 'auvffqnubmjhjsqqnwd', 'iglexamfdtvt', 'kyqhtekrdfcigv', 'elgnstionj', 'rnjifiaoeaweiqoxmsx', 'veozzplakcamuplgpx', 'vnwwgxpvmnqev', 'bkclrgwnzmbut', 'lfdfiuwfrnevaraz', 'bypmwgpbgmsujnlowj', 'qmrsqbaatfzu', 'eaugxiwfddefirhcf', 'lywaxsogirghqgj', 'sgdpknswxysln', 'hjnirpgylrvicvn', 'rzdgauiaqfd', 'cmhggogvznkvwon', 'gikbbcuucfceho', 'hrwroqumokjcb', 'hqsdgjtpfxwzx', 'qmrsqbaatfzu', 'palaxwkqxstdah', 'dzstfixtnfccvwd', 'rsffaewcsxxocl', 'bkclrgwnzmbut', 'vswlswwjpooelqttk', 'ejfeswctcdbrfnqy', 'sfduuipjzhhkvtiv', 'qacecpatcxoibelsaad', 'hjnirpgylrvicvn', 'shrnzqokjsmtkcc', 'rlmeprpzlifivjpdf', 'iysxcgoufz', 'dvlahbxlvr', 'vpkytxfbeaqcioe', 'hjnirpgylrvicvn', 'zxyqmmiqnjnpg', 'mhakcihhthaajuamlg', 'hlloonkdmanq', 'qkhwynrlneksncv', 'maenrdysbritmbtvyy', 'iysxcgoufz', 'qmrsqbaatfzu', 'qacecpatcxoibelsaad', 'rlmeprpzlifivjpdf', 'bkclrgwnzmbut', 'kowvhbqhmthb', 'eyrphlbrkw', 'bkclrgwnzmbut', 'xungqrwaihorcwb', 'cnzvvbicdocbfzcvg', 'cvyebywhzrheav', 'hqsdgjtpfxwzx', 'rlmeprpzlifivjpdf', 'bypmwgpbgmsujnlowj', 'ejfeswctcdbrfnqy', 'xzscqzxmcejqjq', 'hjnirpgylrvicvn', 'xfsjxooclcycwcn', 'uuqokimbilegfjrhzu', 'zxyqmmiqnjnpg', 'sfduuipjzhhkvtiv', 'gikbbcuucfceho', 'sgdpknswxysln', 'xujqjgidmzuilic', 'nddrscobfrojtwew', 'fswnwcgwwzazfbw', 'zrovgoudbnwrougxqz', 'qfvwoqfsoidz', 'iufqqsymxpsopnwuyh', 'pinxwmmeifueviczi', 'mhakcihhthaajuamlg', 'xungqrwaihorcwb']


#strings.extend(strings) 
#queries.extend(queries)

def matchingStrings():#(strings, queries):
    frecuencies = []
    for q in queries: #O(n)
        f = 0
        for s in strings: #O(n**2)
            f += 1 if s == q else 0
        frecuencies.append(f)

    return frecuencies

def matchingStrings2():#(strings, queries):
    counts = {} #O(1) #ab: 2, abc: 1
    for s in strings: #O(n)
        c = counts.get(s, 0) + 1
        counts[s] = c
    
    frecuencies = [0 for _ in queries] #O(n)
    
    i = 0
    for q in queries:  #O(n)
        frecuencies[i] = counts.get(q, 0)
        i += 1
       
    return frecuencies

lp = LineProfiler()
lp.add_function(matchingStrings)
lp.add_function(matchingStrings2)

lp.enable()  
matchingStrings()
matchingStrings2()
lp.disable() 
lp.print_stats()

    
