import numpy as np
import csv


def character_digitization():

    source_file = 'corrected'
    handled_file = 'testing_dataset.csv'

    data_file = open(handled_file, 'w', newline='')
    with open(source_file, 'r') as data_source:
        csv_reader = csv.reader(data_source)
        csv_writer = csv.writer(data_file)
        count = 0
        for row in csv_reader:
            temp_line = np.array(row)
            temp_line[1] = handleProtocol(row)  # 协议类型
            temp_line[2] = handleService(row)  # 服务类型
            temp_line[3] = handleFlag(row)  # 连接状态
            temp_line[41] = handleLabel(row)  # 攻击类型
            csv_writer.writerow(temp_line)
            count += 1
            # print(count,'status:',temp_line[1],temp_line[2],temp_line[3],temp_line[41])
        data_file.close()


def find_index(x, y):
    return [i for i in range(len(y)) if y[i] == x]


# 协议类型
def handleProtocol(input):
    protocol_list = ['tcp', 'udp', 'icmp']
    if input[1] in protocol_list:
        return find_index(input[1], protocol_list)[0]


# 服务类型
def handleService(input):
    service_list = ['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u',
                    'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest',
                    'hostnames',
                    'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell',
                    'ldap',
                    'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', 'netstat', 'nnsp',
                    'nntp',
                    'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i', 'remote_job', 'rje',
                    'shell',
                    'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time',
                    'urh_i', 'urp_i',
                    'uucp', 'uucp_path', 'vmnet', 'whois', 'X11', 'Z39_50', 'icmp']  # ray 加上一个'icmp' 就不用去掉生成后有none的那一行了
    if input[2] in service_list:
        return find_index(input[2], service_list)[0]


# 连接状态
def handleFlag(input):
    flag_list = ['OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH']
    if input[3] in flag_list:
        return find_index(input[3], flag_list)[0]


# 攻击类型
def handleLabel(input):
    label_list_PROBE = ['ipsweep.', 'mscan.', 'nmap.', 'portsweep.', 'saint.', 'satan.']
    label_list_DOS = ['apache2.', 'back.', 'land.', 'mailbomb.', 'neptune.', 'pod.', 'processtable.', 'smurf.',
                      'teardrop.', 'udpstorm.']
    label_list_U2R = ['buffer_overflow.', 'httptunnel.', 'loadmodule.', 'perl.', 'ps.', 'rootkit.', 'sqlattack.', 'xterm.']
    label_list_R2L = ['ftp_write.', 'guess_passwd.', 'imap.', 'multihop.', 'named.', 'phf.', 'sendmail.', 'snmpgetattack.', 'snmpguess.', 'spy.', 'warezclient.', 'warezmaster.', 'worm.', 'xlock.', 'xsnoop.']

    if input[41] == 'normal.':
        return 0
    elif input[41] in label_list_PROBE:
        return 1
    elif input[41] in label_list_DOS:
        return 2
    elif input[41] in label_list_U2R:
        return 3
    elif input[41] in label_list_R2L:
        return 4
    else:
        print("error_lable")
        return 29


if __name__ == '__main__':
    global label_list  # 声明一个全局变量的列表并初始化为空
    label_list = []
    character_digitization()
    print("done")

