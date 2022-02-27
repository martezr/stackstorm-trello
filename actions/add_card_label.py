from lib import action


class AddCardLabelAction(action.BaseAction):
    def run(self, card_id, label_id, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        card = self._client().get_card(card_id)
        card.add_label(label_id)

        return card
