// @flow
import * as React from 'react';
import { ActionApi } from '../ActionApi';

import type {MessageType} from 'components/messages';

type Props = {
  hostid: string,
  children: ({onAction: (action: string, poolNames?: Array<string>, Object, volumes?: {string: Array<string>}) => void, messages: Array<MessageType>} => React.Node),
  bounce?: string,
  callback?: Function,
};

export function VirtualizationPoolsActionApi(props: Props) {
  return (
    <ActionApi
      urlTemplate={ `/rhn/manager/api/systems/details/virtualization/pools/${props.hostid}/`}
      bounce={props.bounce}
      callback={props.callback}
    >
    {
      ({
        onAction: apiAction,
        messages,
      }) => {
        const onAction = (action: string, poolNames?: Array<string>, parameters: Object, volumes?: {string: Array<string>}) => {
          const messageData = volumes == null ?
            Object.assign({ }, parameters, { poolNames }) : Object.assign({ }, parameters, { volumes });
          apiAction((urlTemplate) => {
            const urlBase = volumes == null ? urlTemplate : urlTemplate.replace('/pools/', '/volumes/');
            return `${urlBase}${action}`;
          }, action, messageData);
        }
        return props.children({onAction, messages});
      }
    }
    </ActionApi>
  );
}
VirtualizationPoolsActionApi.defaultProps = {
  bounce: undefined,
  callback: undefined,
  volume: false,
};
