from PyQt5.QtCore import Qt, QAbstractTableModel

class TableModel(QAbstractTableModel):
	def __init__(self, data=[]):
		super().__init__()
		self._data = data
		self.headers = []


	def rowCount(self, index=None):
		return len(self._data)

	def columnCount(self, index=None):
		try:
			return len(self._data[0])
		except IndexError:
			return 0

	def data(self, index, role=Qt.DisplayRole):
		if not index.isValid():
			return None
		if role == Qt.DisplayRole:
			row, col = index.row(), index.column()
			return (self._data[row][col])

	def headerData(self, section, orientation, role):
		if role == Qt.DisplayRole:
			if orientation == Qt.Horizontal:
				return self.headers[section]
			if orientation == Qt.Vertical:
				return section

