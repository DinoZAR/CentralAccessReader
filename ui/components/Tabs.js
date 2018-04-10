import React from 'react';
import PropTypes from 'prop-types';
import { get, isNil } from 'lodash';

import { StyleSheet, css } from '../styles/aphrodite';
import constants from '../styles/constants';

class Tabs extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentTab: get(this.props, 'tabs[0].key', ''),
    };
  }

  componentWillReceiveProps(nextProps) {
    if (nextProps.tabs.every(tab => tab.key !== this.state.currentTab)) {
      this.setState({ currentTab: get(this.nextProps, 'tabs[0].key', '') });
    }
  }

  render() {
    const { tabs, showAdd, onTabClicked, onTabClosed, onAddClicked } = this.props;
    const { currentTab } = this.state;
    const showTab = tabs.find(tab => tab.key === currentTab);
    return (
      <div style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
        <div
          className={css(styles.tabsContainer)}
          style={{ flexShrink: 1, display: 'flex', flexDirection: 'row' }}
        >
          {tabs.map(tab => (
            <div
              key={tab.key}
              className={tab.key === currentTab ? css(styles.tab, styles.activeTab) : css(styles.tab)}
              style={{
                display: 'flex',
                flexDirection: 'row',
                alignItems: 'center',
              }}
              onClick={() => {
                onTabClicked(tab.key);
                this.setState({ currentTab: tab.key });
              }}
            >
              <div
                className={css(styles.tabContent)}
                style={{
                  flex: '1 1 100%',
                  paddingRight: tab.closable ? '0.25rem' : '1rem',
                }}
              >
                {tab.tab}
              </div>
              {tab.closable && (
                <button
                  className={css(styles.closeButton)}
                  style={{ flexShrink: 0 }}
                  onClick={() => {
                    onTabClosed(tab.key);
                  }}
                >
                  <i className="fa fa-times-circle" />
                </button>
              )}
            </div>
          ))}
          {showAdd && (
            <button
              className={css(styles.addButton)}
              onClick={() => { onAddClicked(); }}
            >
              <i className="fa fa-plus fa-2x" />
            </button>
          )}
        </div>
        <div style={{ flex: '1 1 100%', overflow: 'hidden' }}>
          {isNil(showTab) ? null : showTab.content}
        </div>
      </div>
    );
  }
}

Tabs.propTypes = {
  tabs: PropTypes.arrayOf(
    PropTypes.shape({
      key: PropTypes.string.isRequired,
      tab: PropTypes.node.isRequired,
      content: PropTypes.node.isRequired,
      closable: PropTypes.bool,
    })
  ).isRequired,
  showAdd: PropTypes.bool,
  onTabClicked: PropTypes.func,
  onTabClosed: PropTypes.func,
  onAddClicked: PropTypes.func,
};

Tabs.defaultProps = {
  showAdd: false,
  onTabClicked: () => {},
  onTabClosed: () => {},
  onAddClicked: () => {},
};

const styles = StyleSheet.create({
  tabsContainer: {
    backgroundColor: constants.darkerBackgroundColor,
    borderBottom: `1px solid ${constants.darkerBackgroundColor}`,
  },
  tab: {
    color: 'white',
    borderRight: `1px solid ${constants.darkerBackgroundColor}`,
    backgroundColor: constants.backgroundColor,
    cursor: 'pointer',
  },
  tabContent: {
    padding: '0.75rem 1rem',
  },
  closeButton: {
    padding: '0.5rem',
    border: 'none',
    color: 'white',
    fontSize: '1rem',
    background: 'transparent',
    height: '100%',
    cursor: 'pointer',
  },
  addButton: {
    border: 'none',
    borderRight: `1px solid ${constants.darkerBackgroundColor}`,
    backgroundColor: constants.backgroundColor,
    height: '100%',
    color: 'white',
    cursor: 'pointer',
    padding: '0.5rem 1rem',
  },
  activeTab: {
    backgroundColor: constants.lighterBackgroundColor,
  },
});

export default Tabs;
