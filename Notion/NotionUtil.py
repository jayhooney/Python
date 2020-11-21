from notion.block import CollectionViewBlock
from notion.client import NotionClient
from Define.Secret import _MY_NOTION_PAGE_URL_, _MY_TOKEN_V2_


class NotionUtil:

    # def getSchema(self):
    #     return {
    #         # title 항상 존재 해야한다
    #         "title": {"name": "날짜", "type": "date"},
    #         "priority": {"name": "IS_야근", "type": "checkbox"},
    #         "complete_1": {"name": "TASK_TITLE_1", "type": "text"},
    #         "complete_2": {"name": "TASK_TITLE_2", "type": "text"},
    #         "complete_3": {"name": "TASK_TITLE_3", "type": "text"},
    #         "complete_4": {"name": "TASK_TITLE_4", "type": "text"},
    #         "complete_5": {"name": "TASK_TITLE_5", "type": "text"},
    #         "complete_6": {"name": "TASK_TITLE_6", "type": "text"},
    #         "complete_7": {"name": "TASK_TITLE_7", "type": "text"},

    #     }

    def Start(self):
        client = NotionClient(token_v2=_MY_TOKEN_V2_)
        page = client.get_block(_MY_NOTION_PAGE_URL_)
        page.title = "MY_WORK_RECORD"

        row = page.collection.add_row()
        row.set_property('날짜', "2020/11/20 9:00-18:00")
        row.set_property('IS_야근', True)
        row.set_property('TASK_TITLE_1', 'dev_1')
        row.set_property('TASK_TITLE_2', 'dev_1')
        row.set_property('TASK_TITLE_3', 'dev_1')
        row.set_property('TASK_TITLE_4', 'dev_1')
        row.set_property('TASK_TITLE_5', 'dev_1')
        row.set_property('TASK_TITLE_6', 'dev_1')
        row.set_property('TASK_TITLE_7', 'dev_1')
        return
