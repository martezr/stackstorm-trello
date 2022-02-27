from lib import action


class AddCardLabelAction(action.BaseAction):
    def run(self, card_id, board_id, label_id, api_key=None, token=None):
        if api_key:
            self._set_creds(api_key=api_key, token=token)

        card = self._client().get_card(card_id)
        board = self._client().get_board(board_id)
        outlabel = ""
        for label in board.get_labels('all'):
            if label.id == label_id:
                outlabel = label
        card.add_label(outlabel)

        return card
