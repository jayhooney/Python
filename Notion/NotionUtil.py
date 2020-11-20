from notion.block import CollectionViewBlock
from notion.client import NotionClient
from Define.Secret import _MY_NOTION_PAGE_URL_, _MY_TOKEN_V2_


class NotionUtil:

    def getSchema(self):
        return {
            # title 항상 존재 해야한다
            "title": {"name": "날짜", "type": "date"},
            "priority": {"name": "IS_야근", "type": "checkbox"},
            "complete_1": {"name": "JOB_TITLE_1", "type": "text"},
            "complete_2": {"name": "JOB_TITLE_2", "type": "text"},
            "complete_3": {"name": "JOB_TITLE_3", "type": "text"},
            "complete_4": {"name": "JOB_TITLE_4", "type": "text"},
            "complete_5": {"name": "JOB_TITLE_5", "type": "text"},
            "complete_6": {"name": "JOB_TITLE_6", "type": "text"},
            "complete_7": {"name": "JOB_TITLE_7", "type": "text"},

        }

    def Start(self):
        client = NotionClient(token_v2=_MY_TOKEN_V2_)
        page = client.get_block(_MY_NOTION_PAGE_URL_)

        child = page.children.add_new(CollectionViewBlock)
        child.collection = client.get_collection(
            client.create_record(
                "collection", parent=child, schema=self.getSchema())
        )
        child.title = 'TEST TABLE'
        child.views.add_new(view_type="table")

        row = child.collection.add_row()
        row.set_property('날짜', "2020/11/20 9:00-18:00")
        row.set_property('IS_야근', True)
        row.set_property('JOB_TITLE_1', 'dev_1')
        row.set_property('JOB_TITLE_2', 'dev_1')
        row.set_property('JOB_TITLE_3', 'dev_1')
        row.set_property('JOB_TITLE_4', 'dev_1')
        row.set_property('JOB_TITLE_5', 'dev_1')
        row.set_property('JOB_TITLE_6', 'dev_1')
        row.set_property('JOB_TITLE_7', 'dev_1')
        return
