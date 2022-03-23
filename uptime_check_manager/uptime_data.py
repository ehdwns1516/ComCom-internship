uptimecheck_infos = dict()
removed_host_list = list()


def get_uptimecheck_infos():
    return uptimecheck_infos


def get_removed_host_list():
    return removed_host_list


def add_uptimecheck_info(host, incident_id, incident_url, state, arrived_time):
    if host not in uptimecheck_infos:
        uptimecheck_infos[host] = [incident_id, incident_url, state, arrived_time]


def add_removed_host(host):
    if host not in removed_host_list:
        removed_host_list.append(host)


def delete_uptimecheck_info(host):
    if host in uptimecheck_infos:
        del uptimecheck_infos[host]


def delete_removed_host(host):
    if host in removed_host_list:
        removed_host_list.remove(host)

