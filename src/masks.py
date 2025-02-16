from typing import List, Dict, Any, Tuple


def filter_by_state(list_logs: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """Функция принимает список словарей и возвращает список с ключом выбранного значения"""
    new_list_1 = []
    new_list_2 = []
    for i in list_logs:
        if i.get('state') == 'EXECUTED':
            new_list_1.append(i)
        else:
            new_list_2.append(i)
    return new_list_1, new_list_2


list_1, list_2 = filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
print(list_1)
print(list_2)


def sort_by_date(data_logs: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция принимает список словарей и возвращает список, отсортированный по дате"""
    return sorted(data_logs, key=lambda x: x["date"], reverse=reverse)


list_1 = sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])
print(list_1)
