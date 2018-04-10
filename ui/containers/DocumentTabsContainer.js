import { connect } from 'react-redux';

import Tabs from '../components/Tabs';
import { openFile } from '../actions/file';

const mapDispatchToProps = {
  onAddClicked: openFile,
};

export default connect(() => ({}), mapDispatchToProps)(Tabs);
