
from attr import dataclass

#s4 teng https://t.me/shuraim1/https:/
#S5 teng https://t.me/alquran30juzsaadalghamidi/5
#s6 teng https://t.me/bandar_abdulaziz_balilah/5 
#s7 teng https://t.me/Idriss_Akbar/388
#s8 teng https://t.me/yasseraldosari_mp3/2

sura = {
     '0': {'s1':'42', 's2':'257', 's3':'18', 's4':'3', 's5':'5', 's6':'5', 's7':'388', 's8':'2',},
     '1': {'s1':'42', 's2':'257', 's3':'18', 's4':'3', 's5':'5', 's6':'5', 's7':'388', 's8':'2',},
     '2': {'s1':'43', 's2':'258', 's3':'19', 's4':'4', 's5':'6', 's6':'6', 's7':'389', 's8':'3',},
     '3': {'s1':'44', 's2':'259', 's3':'20', 's4':'5', 's5':'7', 's6':'7', 's7':'390', 's8':'4',},
     '4': {'s1':'45', 's2':'260', 's3':'21', 's4':'6', 's5':'8', 's6':'8', 's7':'391', 's8':'5',},
     '5': {'s1':'46', 's2':'261', 's3':'22', 's4':'7', 's5':'9', 's6':'9', 's7':'392', 's8':'6',},
     '6': {'s1':'47', 's2':'262', 's3':'23', 's4':'8', 's5':'10', 's6':'10', 's7':'393', 's8':'7',},
     '7': {'s1':'48', 's2':'263', 's3':'24', 's4':'9', 's5':'11', 's6':'11', 's7':'394', 's8':'8',}, 
     '8': {'s1':'49', 's2':'264', 's3':'25', 's4':'10', 's5':'12', 's6':'12', 's7':'395', 's8':'9',}, 
     '9': {'s1':'50', 's2':'265', 's3':'26', 's4':'11', 's5':'13', 's6':'13', 's7':'396', 's8':'10',}, 
     '10': {'s1':'51', 's2':'266', 's3':'27', 's4':'12', 's5':'14', 's6':'14', 's7':'397', 's8':'11',}, 
     '11': {'s1': '52', 's2':'267', 's3':'28', 's4':'13', 's5':'15', 's6':'15', 's7':'398', 's8':'12',}, 
     '12': {'s1':'53', 's2':'268', 's3':'29', 's4':'14', 's5':'16', 's6':'16', 's7':'399', 's8':'13',}, 
     '13': {'s1': '54', 's2':'269', 's3':'30', 's4':'15', 's5':'17', 's6':'17', 's7':'401', 's8':'14',}, 
     '14': {'s1':'55', 's2':'270', 's3':'31', 's4':'16', 's5':'18', 's6':'18', 's7':'402', 's8':'15',}, 
     '15': {'s1':'56', 's2':'271', 's3':'32', 's4':'17', 's5':'19', 's6':'19', 's7':'403', 's8':'16',}, 
     '16': {'s1':'59', 's2':'272', 's3':'33', 's4':'18', 's5':'20', 's6':'20', 's7':'404', 's8':'17',}, 
     '17': {'s1':'60', 's2':'273', 's3':'34', 's4':'19', 's5':'21', 's6':'21', 's7':'405', 's8':'18',}, 
     '18' : {'s1':'61', 's2':'274', 's3':'35', 's4':'20', 's5':'22', 's6':'22', 's7':'406', 's8':'19',}, 
     '19': {'s1':'62', 's2':'275', 's3':'36', 's4':'21', 's5':'23', 's6':'23', 's7':'407', 's8':'20',}, 
     '20': {'s1':'63', 's2':'276', 's3':'37', 's4':'22', 's5':'24', 's6':'24', 's7':'408', 's8':'21',}, 
     '21': {'s1':'64', 's2':'277', 's3':'38', 's4':'23', 's5':'25', 's6':'25', 's7':'409', 's8':'22',}, 
     '22': {'s1':'65', 's2':'278', 's3':'39', 's4':'24', 's5':'26', 's6':'26', 's7':'410', 's8':'23',}, 
     '23': {'s1':'66', 's2':'279', 's3':'40', 's4':'25', 's5':'27', 's6':'27', 's7':'411', 's8':'24',}, 
     '24': {'s1':'67', 's2':'280', 's3':'41', 's4':'26', 's5':'28', 's6':'28', 's7':'412', 's8':'25',}, 
     '25': {'s1':'68', 's2':'281', 's3':'42', 's4':'27', 's5':'29', 's6':'29', 's7':'413', 's8':'26',},
     '26': {'s1':'69', 's2':'282', 's3':'43', 's4':'28', 's5':'30', 's6':'30', 's7':'414', 's8':'27',},
     '27': {'s1':'70', 's2':'283', 's3':'44', 's4':'29', 's5':'31', 's6':'31', 's7':'415', 's8':'28',}, 
     '28': {'s1':'71', 's2':'284', 's3':'45', 's4':'30', 's5':'32', 's6':'32', 's7':'416', 's8':'29',}, 
     '29': {'s1':'72', 's2':'285', 's3':'46', 's4':'31', 's5':'33', 's6':'33', 's7':'417', 's8':'30',},
     '30': {'s1':'73', 's2':'286', 's3':'47', 's4':'32', 's5':'34', 's6':'34', 's7':'418', 's8':'31',},
     '31': {'s1':'74', 's2':'287', 's3':'48', 's4':'33', 's5':'35', 's6':'35', 's7':'419', 's8':'32',},
     '32': {'s1':'75', 's2':'288', 's3':'49', 's4':'34', 's5':'36', 's6':'36', 's7':'420', 's8':'33',},
     '33': {'s1':'76', 's2':'289', 's3':'50', 's4':'35', 's5':'37', 's6':'37', 's7':'421', 's8':'34',},
     '34': {'s1':'77', 's2':'290', 's3':'51', 's4':'36', 's5':'38', 's6':'38', 's7':'422', 's8':'35',},
     '35': {'s1':'78', 's2':'291', 's3':'52', 's4':'37', 's5':'39', 's6':'39', 's7':'423', 's8':'36',},
     '36': {'s1':'79', 's2':'292', 's3':'53', 's4':'38', 's5':'40', 's6':'40', 's7':'424', 's8':'37',}, 
     '37': {'s1':'80', 's2':'293', 's3':'54', 's4':'39', 's5':'41', 's6':'41', 's7':'425', 's8':'38',},
     '38': {'s1':'81', 's2':'294', 's3':'55', 's4':'40', 's5':'42', 's6':'42', 's7':'426', 's8':'39',},
     '39': {'s1':'82', 's2':'295', 's3':'56', 's4':'41', 's5':'43', 's6':'43', 's7':'427', 's8':'40',},
     '40': {'s1':'83', 's2':'296', 's3':'57', 's4':'42', 's5':'44', 's6':'44', 's7':'428', 's8':'41',},
     '41': {'s1':'84', 's2':'297', 's3':'58', 's4':'43', 's5':'45', 's6':'45', 's7':'429', 's8':'42',},
     '42': {'s1':'85', 's2':'298', 's3':'59', 's4':'44', 's5':'46', 's6':'46', 's7':'430', 's8':'43',},
     '43': {'s1':'86', 's2':'299', 's3':'60', 's4':'45', 's5':'47', 's6':'47', 's7':'431', 's8':'44',},
     '44': {'s1':'87', 's2':'300', 's3':'61', 's4':'46', 's5':'48', 's6':'48', 's7':'432', 's8':'45',},
     '45': {'s1':'88', 's2':'301', 's3':'62', 's4':'47', 's5':'49', 's6':'49', 's7':'433', 's8':'46',},  
     '46': {'s1':'89', 's2':'302', 's3':'63', 's4':'48', 's5':'50', 's6':'50', 's7':'434', 's8':'47',},
     '47': {'s1':'90', 's2':'303', 's3':'64', 's4':'49', 's5':'51', 's6':'51', 's7':'435', 's8':'48',}, 
     '48': {'s1':'91', 's2':'304', 's3':'65', 's4':'50', 's5':'52', 's6':'52', 's7':'436', 's8':'49',},
     '49': {'s1':'92', 's2':'305', 's3':'66', 's4':'51', 's5':'53', 's6':'53', 's7':'437', 's8':'50',}, 
     '50': {'s1':'93', 's2':'306', 's3':'67', 's4':'52', 's5':'54', 's6':'54', 's7':'438', 's8':'51',}, 
     '51': {'s1':'94', 's2':'307', 's3':'68', 's4':'53', 's5':'55', 's6':'55', 's7':'439', 's8':'52',},
     '52': {'s1':'95', 's2':'308', 's3':'69', 's4':'54', 's5':'56', 's6':'56', 's7':'440', 's8':'53',},
     '53': {'s1':'96', 's2':'309', 's3':'70', 's4':'55', 's5':'57', 's6':'57', 's7':'441', 's8':'54',}, 
     '54': {'s1':'97', 's2':'310', 's3':'71', 's4':'56', 's5':'58', 's6':'58', 's7':'442', 's8':'55',},
     '55': {'s1':'98', 's2':'311', 's3':'72', 's4':'57', 's5':'59', 's6':'59', 's7':'443', 's8':'56',},
     '56': {'s1':'99', 's2':'312', 's3':'73', 's4':'58', 's5':'60', 's6':'60', 's7':'444', 's8':'57',},
     '57': {'s1':'100', 's2':'313', 's3':'74', 's4':'59', 's5':'61', 's6':'61', 's7':'445', 's8':'58',},
     '58': {'s1':'101', 's2':'314', 's3':'75', 's4':'60', 's5':'62', 's6':'62', 's7':'446', 's8':'59',},
     '59': {'s1':'102', 's2':'315', 's3':'76', 's4':'61', 's5':'63', 's6':'63', 's7':'447', 's8':'60',}, 
     '60': {'s1':'103', 's2':'316', 's3':'77', 's4':'62', 's5':'64', 's6':'64', 's7':'448', 's8':'61',}, 
    #61 inlinekeyboard starts in here 

     '61': {'s1':'104', 's2':'317', 's3':'78', 's4':'63', 's5':'65', 's6':'65', 's7':'449', 's8':'62',},
     '62': {'s1':'105', 's2':'318', 's3':'79', 's4':'64', 's5':'66', 's6':'66', 's7':'450', 's8':'63',}, 
     '63': {'s1':'106', 's2':'319', 's3':'80', 's4':'65', 's5':'67', 's6':'67', 's7':'451', 's8':'64',},
     '64': {'s1':'107', 's2':'320', 's3':'81', 's4':'66', 's5':'68', 's6':'68', 's7':'452', 's8':'65',},
     '65': {'s1':'108', 's2':'321', 's3':'82', 's4':'67', 's5':'69', 's6':'69', 's7':'453', 's8':'66',},
     '66': {'s1':'109', 's2':'322', 's3':'83', 's4':'68', 's5':'70', 's6':'70', 's7':'454', 's8':'67',}, 
     '67': {'s1':'110', 's2':'323', 's3':'84', 's4':'69', 's5':'71', 's6':'72', 's7':'455', 's8':'68',},
     '68': {'s1':'111', 's2':'324', 's3':'85', 's4':'70', 's5':'72', 's6':'73', 's7':'456', 's8':'69',},
     '69': {'s1':'112', 's2':'325', 's3':'86', 's4':'71', 's5':'73', 's6':'74', 's7':'457', 's8':'70',}, 
     '70': {'s1':'113', 's2':'326', 's3':'87', 's4':'72', 's5':'74', 's6':'75', 's7':'458', 's8':'71',}, 
     '71': {'s1':'114', 's2':'327', 's3':'88', 's4':'73', 's5':'75', 's6':'76', 's7':'459', 's8':'72',}, 
     '72': {'s1':'115', 's2':'328', 's3':'89', 's4':'74', 's5':'76', 's6':'77', 's7':'460', 's8':'73',}, 
     '73': {'s1':'116', 's2':'329', 's3':'90', 's4':'75', 's5':'77', 's6':'78', 's7':'461', 's8':'74',}, 
     '74': {'s1':'117', 's2':'330', 's3':'91', 's4':'76', 's5':'78', 's6':'79', 's7':'462', 's8':'75',}, 
     '75': {'s1':'118', 's2':'331', 's3':'92', 's4':'77', 's5':'79', 's6':'80', 's7':'463', 's8':'76',}, 
     '76': {'s1':'119', 's2':'332', 's3':'93', 's4':'78', 's5':'80', 's6':'81', 's7':'464', 's8':'77',}, 
     '77': {'s1':'120', 's2':'333', 's3':'94', 's4':'79', 's5':'81', 's6':'82', 's7':'465', 's8':'78',}, 
     '78': {'s1':'121', 's2':'334', 's3':'95', 's4':'80', 's5':'82', 's6':'83', 's7':'466', 's8':'79',}, 
     '79': {'s1':'122', 's2':'335', 's3':'96', 's4':'81', 's5':'83', 's6':'84', 's7':'467', 's8':'80',}, 
     '80': {'s1':'123', 's2':'336', 's3':'97', 's4':'82', 's5':'84', 's6':'85', 's7':'468', 's8':'81',}, 
     '81': {'s1':'124', 's2':'337', 's3':'98', 's4':'83', 's5':'85', 's6':'86', 's7':'469', 's8':'82',}, 
     '82': {'s1':'125', 's2':'338', 's3':'99', 's4':'84', 's5':'86', 's6':'87', 's7':'470', 's8':'83',}, 
     '83': {'s1':'126', 's2':'339', 's3':'100', 's4':'85', 's5':'87', 's6':'88', 's7':'471', 's8':'84',},
     '84': {'s1':'127', 's2':'340', 's3':'101', 's4':'86', 's5':'88', 's6':'89', 's7':'472', 's8':'85',}, 
     '85': {'s1':'128', 's2':'341', 's3':'102', 's4':'87', 's5':'89', 's6':'90', 's7':'473', 's8':'86',}, 
     '86': {'s1':'129', 's2':'342', 's3':'103', 's4':'88', 's5':'90', 's6':'91', 's7':'474', 's8':'87',},
     '87': {'s1':'130', 's2':'343', 's3':'104', 's4':'89', 's5':'91', 's6':'92', 's7':'475', 's8':'88',}, 
     '88': {'s1':'131', 's2':'344', 's3':'105', 's4':'90', 's5':'92', 's6':'93', 's7':'476', 's8':'89',}, 
     '89': {'s1':'132', 's2':'345', 's3':'106', 's4':'91', 's5':'93', 's6':'94', 's7':'477', 's8':'90',}, 
     '90': {'s1':'133', 's2':'346', 's3':'107', 's4':'92', 's5':'94', 's6':'95', 's7':'478', 's8':'91',}, 
     '91': {'s1':'134', 's2':'347', 's3':'108', 's4':'93', 's5':'95', 's6':'96', 's7':'479', 's8':'92',}, 
     '92': {'s1':'135', 's2':'348', 's3':'109', 's4':'94', 's5':'96', 's6':'97', 's7':'480', 's8':'93',}, 
     '93': {'s1':'136', 's2':'349', 's3':'110', 's4':'95', 's5':'97', 's6':'98', 's7':'481', 's8':'94',}, 
     '94': {'s1':'137', 's2':'350', 's3':'111', 's4':'96', 's5':'98', 's6':'99', 's7':'482', 's8':'95',}, 
     '95': {'s1':'138', 's2':'351', 's3':'112', 's4':'97', 's5':'99', 's6':'100', 's7':'483', 's8':'96',}, 
     '96': {'s1':'139', 's2':'352', 's3':'113', 's4':'98', 's5':'100', 's6':'101', 's7':'484', 's8':'97',}, 
     '97': {'s1':'140', 's2':'353', 's3':'114', 's4':'99', 's5':'101', 's6':'102', 's7':'485', 's8':'98',}, 
     '98': {'s1':'141', 's2':'354', 's3':'115', 's4':'100', 's5':'102', 's6':'103', 's7':'486', 's8':'99',},
     '99': {'s1':'142', 's2':'355', 's3':'116', 's4':'101', 's5':'103', 's6':'104', 's7':'487', 's8':'100',}, 
     '100': {'s1':'143', 's2':'356', 's3':'117', 's4':'102', 's5':'104', 's6':'105', 's7':'488', 's8':'101',}, 
     '101': {'s1':'144', 's2':'357', 's3':'118', 's4':'103', 's5':'105', 's6':'106', 's7':'489', 's8':'102',}, 
     '102': {'s1':'145', 's2':'358', 's3':'119', 's4':'104', 's5':'106', 's6':'107', 's7':'490', 's8':'103',}, 
     '103': {'s1':'146', 's2':'359', 's3':'120', 's4':'105', 's5':'107', 's6':'108', 's7':'491', 's8':'104',}, 
     '104': {'s1':'147', 's2':'360', 's3':'121', 's4':'106', 's5':'108', 's6':'109', 's7':'492', 's8':'105',}, 
     '105': {'s1':'148', 's2':'361', 's3':'122', 's4':'107', 's5':'109', 's6':'110', 's7':'493', 's8':'106',}, 
     '106': {'s1':'149', 's2':'362', 's3':'123', 's4':'108', 's5':'110', 's6':'111', 's7':'494', 's8':'107',}, 
     '107': {'s1':'150', 's2':'363', 's3':'124', 's4':'109', 's5':'111', 's6':'112', 's7':'495', 's8':'108',}, 
     '108': {'s1':'151', 's2':'364', 's3':'125', 's4':'110', 's5':'112', 's6':'113', 's7':'496', 's8':'109',}, 
     '109': {'s1':'152', 's2':'365', 's3':'126', 's4':'111', 's5':'113', 's6':'114', 's7':'497', 's8':'110',}, 
     '110': {'s1':'153', 's2':'366', 's3':'127', 's4':'112', 's5':'114', 's6':'115', 's7':'498', 's8':'111',}, 
     '111': {'s1':'154', 's2':'367', 's3':'128', 's4':'113', 's5':'115', 's6':'116', 's7':'499', 's8':'112',}, 
     '112': {'s1':'155', 's2':'368', 's3':'129', 's4':'114', 's5':'116', 's6':'117', 's7':'500', 's8':'113',}, 
     '113': {'s1':'156', 's2':'369', 's3':'130', 's4':'115', 's5':'117', 's6':'118', 's7':'501', 's8':'114',}, 
     '114': {'s1':'157', 's2':'370', 's3':'131', 's4':'116', 's5':'118', 's6':'119', 's7':'502', 's8':'115',}
     }
    
bbc = {'22':'11', 'n':{
    '55':'56',
    '55':'58',
    '55':'59',
    '55':'555',


}}




hmuchun = {
      'hm5':{
            'rep':257,
            'rep2':287,
            
      },
      'hm6':{
            'rep':288,
            'rep2':317,
      },
      'hm7':{
            'rep':317,
            'rep2':347,
      },
      'hm8':{
            'rep':347,
            'rep2':371,
      },
      'hm9':{
            'rep':18,
            'rep2':48,
            
      },
      'hm10':{
            'rep':48,
            'rep2':78,
      },
      'hm11':{
            'rep':78,
            'rep2':108,
      },
      'hm12':{
            'rep':108,
            'rep2':137,
      },

}

      