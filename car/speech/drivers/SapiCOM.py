# -*- coding: utf-8 -*-
# Created by makepy.py version 0.5.01
# By python version 2.7.3 (default, Apr 10 2012, 23:24:47) [MSC v.1500 64 bit (AMD64)]
# From type library 'sapi.dll'
# On Thu May 02 15:00:03 2013
'Microsoft Speech Object Library'
makepy_version = '0.5.01'
python_version = 0x20703f0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{C866CA3A-32F7-11D2-9602-00C04F8EE628}')
MajorVersion = 5
MinorVersion = 4
LibraryFlags = 8
LCID = 0x0

class constants:
	DISPID_SRGCmdLoadFromFile     =7          # from enum DISPIDSPRG
	DISPID_SRGCmdLoadFromMemory   =10         # from enum DISPIDSPRG
	DISPID_SRGCmdLoadFromObject   =8          # from enum DISPIDSPRG
	DISPID_SRGCmdLoadFromProprietaryGrammar=11         # from enum DISPIDSPRG
	DISPID_SRGCmdLoadFromResource =9          # from enum DISPIDSPRG
	DISPID_SRGCmdSetRuleIdState   =13         # from enum DISPIDSPRG
	DISPID_SRGCmdSetRuleState     =12         # from enum DISPIDSPRG
	DISPID_SRGCommit              =6          # from enum DISPIDSPRG
	DISPID_SRGDictationLoad       =14         # from enum DISPIDSPRG
	DISPID_SRGDictationSetState   =16         # from enum DISPIDSPRG
	DISPID_SRGDictationUnload     =15         # from enum DISPIDSPRG
	DISPID_SRGId                  =1          # from enum DISPIDSPRG
	DISPID_SRGIsPronounceable     =19         # from enum DISPIDSPRG
	DISPID_SRGRecoContext         =2          # from enum DISPIDSPRG
	DISPID_SRGReset               =5          # from enum DISPIDSPRG
	DISPID_SRGRules               =4          # from enum DISPIDSPRG
	DISPID_SRGSetTextSelection    =18         # from enum DISPIDSPRG
	DISPID_SRGSetWordSequenceData =17         # from enum DISPIDSPRG
	DISPID_SRGState               =3          # from enum DISPIDSPRG
	DISPIDSPTSI_ActiveLength      =2          # from enum DISPIDSPTSI
	DISPIDSPTSI_ActiveOffset      =1          # from enum DISPIDSPTSI
	DISPIDSPTSI_SelectionLength   =4          # from enum DISPIDSPTSI
	DISPIDSPTSI_SelectionOffset   =3          # from enum DISPIDSPTSI
	DISPID_SABufferInfo           =201        # from enum DISPID_SpeechAudio
	DISPID_SABufferNotifySize     =204        # from enum DISPID_SpeechAudio
	DISPID_SADefaultFormat        =202        # from enum DISPID_SpeechAudio
	DISPID_SAEventHandle          =205        # from enum DISPID_SpeechAudio
	DISPID_SASetState             =206        # from enum DISPID_SpeechAudio
	DISPID_SAStatus               =200        # from enum DISPID_SpeechAudio
	DISPID_SAVolume               =203        # from enum DISPID_SpeechAudio
	DISPID_SABIBufferSize         =2          # from enum DISPID_SpeechAudioBufferInfo
	DISPID_SABIEventBias          =3          # from enum DISPID_SpeechAudioBufferInfo
	DISPID_SABIMinNotification    =1          # from enum DISPID_SpeechAudioBufferInfo
	DISPID_SAFGetWaveFormatEx     =3          # from enum DISPID_SpeechAudioFormat
	DISPID_SAFGuid                =2          # from enum DISPID_SpeechAudioFormat
	DISPID_SAFSetWaveFormatEx     =4          # from enum DISPID_SpeechAudioFormat
	DISPID_SAFType                =1          # from enum DISPID_SpeechAudioFormat
	DISPID_SASCurrentDevicePosition=5          # from enum DISPID_SpeechAudioStatus
	DISPID_SASCurrentSeekPosition =4          # from enum DISPID_SpeechAudioStatus
	DISPID_SASFreeBufferSpace     =1          # from enum DISPID_SpeechAudioStatus
	DISPID_SASNonBlockingIO       =2          # from enum DISPID_SpeechAudioStatus
	DISPID_SASState               =3          # from enum DISPID_SpeechAudioStatus
	DISPID_SBSFormat              =1          # from enum DISPID_SpeechBaseStream
	DISPID_SBSRead                =2          # from enum DISPID_SpeechBaseStream
	DISPID_SBSSeek                =4          # from enum DISPID_SpeechBaseStream
	DISPID_SBSWrite               =3          # from enum DISPID_SpeechBaseStream
	DISPID_SCSBaseStream          =100        # from enum DISPID_SpeechCustomStream
	DISPID_SDKCreateKey           =8          # from enum DISPID_SpeechDataKey
	DISPID_SDKDeleteKey           =9          # from enum DISPID_SpeechDataKey
	DISPID_SDKDeleteValue         =10         # from enum DISPID_SpeechDataKey
	DISPID_SDKEnumKeys            =11         # from enum DISPID_SpeechDataKey
	DISPID_SDKEnumValues          =12         # from enum DISPID_SpeechDataKey
	DISPID_SDKGetBinaryValue      =2          # from enum DISPID_SpeechDataKey
	DISPID_SDKGetStringValue      =4          # from enum DISPID_SpeechDataKey
	DISPID_SDKGetlongValue        =6          # from enum DISPID_SpeechDataKey
	DISPID_SDKOpenKey             =7          # from enum DISPID_SpeechDataKey
	DISPID_SDKSetBinaryValue      =1          # from enum DISPID_SpeechDataKey
	DISPID_SDKSetLongValue        =5          # from enum DISPID_SpeechDataKey
	DISPID_SDKSetStringValue      =3          # from enum DISPID_SpeechDataKey
	DISPID_SFSClose               =101        # from enum DISPID_SpeechFileStream
	DISPID_SFSOpen                =100        # from enum DISPID_SpeechFileStream
	DISPID_SGRAddResource         =6          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRAddState            =7          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRAttributes          =1          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRClear               =5          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRId                  =4          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRInitialState        =2          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRName                =3          # from enum DISPID_SpeechGrammarRule
	DISPID_SGRSAddRuleTransition  =4          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSAddSpecialTransition=5          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSAddWordTransition  =3          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSRule               =1          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSTransitions        =2          # from enum DISPID_SpeechGrammarRuleState
	DISPID_SGRSTNextState         =8          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTPropertyId        =6          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTPropertyName      =5          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTPropertyValue     =7          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTRule              =3          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTText              =2          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTType              =1          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTWeight            =4          # from enum DISPID_SpeechGrammarRuleStateTransition
	DISPID_SGRSTsCount            =1          # from enum DISPID_SpeechGrammarRuleStateTransitions
	DISPID_SGRSTsItem             =0          # from enum DISPID_SpeechGrammarRuleStateTransitions
	DISPID_SGRSTs_NewEnum         =-4         # from enum DISPID_SpeechGrammarRuleStateTransitions
	DISPID_SGRsAdd                =3          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsCommit             =4          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsCommitAndSave      =5          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsCount              =1          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsDynamic            =2          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsFindRule           =6          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRsItem               =0          # from enum DISPID_SpeechGrammarRules
	DISPID_SGRs_NewEnum           =-4         # from enum DISPID_SpeechGrammarRules
	DISPID_SLAddPronunciation     =3          # from enum DISPID_SpeechLexicon
	DISPID_SLAddPronunciationByPhoneIds=4          # from enum DISPID_SpeechLexicon
	DISPID_SLGenerationId         =1          # from enum DISPID_SpeechLexicon
	DISPID_SLGetGenerationChange  =8          # from enum DISPID_SpeechLexicon
	DISPID_SLGetPronunciations    =7          # from enum DISPID_SpeechLexicon
	DISPID_SLGetWords             =2          # from enum DISPID_SpeechLexicon
	DISPID_SLRemovePronunciation  =5          # from enum DISPID_SpeechLexicon
	DISPID_SLRemovePronunciationByPhoneIds=6          # from enum DISPID_SpeechLexicon
	DISPID_SLPsCount              =1          # from enum DISPID_SpeechLexiconProns
	DISPID_SLPsItem               =0          # from enum DISPID_SpeechLexiconProns
	DISPID_SLPs_NewEnum           =-4         # from enum DISPID_SpeechLexiconProns
	DISPID_SLPLangId              =2          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLPPartOfSpeech        =3          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLPPhoneIds            =4          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLPSymbolic            =5          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLPType                =1          # from enum DISPID_SpeechLexiconPronunciation
	DISPID_SLWLangId              =1          # from enum DISPID_SpeechLexiconWord
	DISPID_SLWPronunciations      =4          # from enum DISPID_SpeechLexiconWord
	DISPID_SLWType                =2          # from enum DISPID_SpeechLexiconWord
	DISPID_SLWWord                =3          # from enum DISPID_SpeechLexiconWord
	DISPID_SLWsCount              =1          # from enum DISPID_SpeechLexiconWords
	DISPID_SLWsItem               =0          # from enum DISPID_SpeechLexiconWords
	DISPID_SLWs_NewEnum           =-4         # from enum DISPID_SpeechLexiconWords
	DISPID_SMSADeviceId           =300        # from enum DISPID_SpeechMMSysAudio
	DISPID_SMSALineId             =301        # from enum DISPID_SpeechMMSysAudio
	DISPID_SMSAMMHandle           =302        # from enum DISPID_SpeechMMSysAudio
	DISPID_SMSGetData             =101        # from enum DISPID_SpeechMemoryStream
	DISPID_SMSSetData             =100        # from enum DISPID_SpeechMemoryStream
	DISPID_SOTCategory            =3          # from enum DISPID_SpeechObjectToken
	DISPID_SOTCreateInstance      =7          # from enum DISPID_SpeechObjectToken
	DISPID_SOTDataKey             =2          # from enum DISPID_SpeechObjectToken
	DISPID_SOTDisplayUI           =12         # from enum DISPID_SpeechObjectToken
	DISPID_SOTGetAttribute        =6          # from enum DISPID_SpeechObjectToken
	DISPID_SOTGetDescription      =4          # from enum DISPID_SpeechObjectToken
	DISPID_SOTGetStorageFileName  =9          # from enum DISPID_SpeechObjectToken
	DISPID_SOTId                  =1          # from enum DISPID_SpeechObjectToken
	DISPID_SOTIsUISupported       =11         # from enum DISPID_SpeechObjectToken
	DISPID_SOTMatchesAttributes   =13         # from enum DISPID_SpeechObjectToken
	DISPID_SOTRemove              =8          # from enum DISPID_SpeechObjectToken
	DISPID_SOTRemoveStorageFileName=10         # from enum DISPID_SpeechObjectToken
	DISPID_SOTSetId               =5          # from enum DISPID_SpeechObjectToken
	DISPID_SOTCDefault            =2          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTCEnumerateTokens    =5          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTCGetDataKey         =4          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTCId                 =1          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTCSetId              =3          # from enum DISPID_SpeechObjectTokenCategory
	DISPID_SOTsCount              =1          # from enum DISPID_SpeechObjectTokens
	DISPID_SOTsItem               =0          # from enum DISPID_SpeechObjectTokens
	DISPID_SOTs_NewEnum           =-4         # from enum DISPID_SpeechObjectTokens
	DISPID_SPCIdToPhone           =3          # from enum DISPID_SpeechPhoneConverter
	DISPID_SPCLangId              =1          # from enum DISPID_SpeechPhoneConverter
	DISPID_SPCPhoneToId           =2          # from enum DISPID_SpeechPhoneConverter
	DISPID_SPACommit              =5          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPANumberOfElementsInResult=3          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPAPhraseInfo          =4          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPARecoResult          =1          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPAStartElementInResult=2          # from enum DISPID_SpeechPhraseAlternate
	DISPID_SPAsCount              =1          # from enum DISPID_SpeechPhraseAlternates
	DISPID_SPAsItem               =0          # from enum DISPID_SpeechPhraseAlternates
	DISPID_SPAs_NewEnum           =-4         # from enum DISPID_SpeechPhraseAlternates
	DISPID_SPPBRestorePhraseFromMemory=1          # from enum DISPID_SpeechPhraseBuilder
	DISPID_SPEActualConfidence    =12         # from enum DISPID_SpeechPhraseElement
	DISPID_SPEAudioSizeBytes      =4          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEAudioSizeTime       =2          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEAudioStreamOffset   =3          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEAudioTimeOffset     =1          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEDisplayAttributes   =10         # from enum DISPID_SpeechPhraseElement
	DISPID_SPEDisplayText         =7          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEEngineConfidence    =13         # from enum DISPID_SpeechPhraseElement
	DISPID_SPELexicalForm         =8          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEPronunciation       =9          # from enum DISPID_SpeechPhraseElement
	DISPID_SPERequiredConfidence  =11         # from enum DISPID_SpeechPhraseElement
	DISPID_SPERetainedSizeBytes   =6          # from enum DISPID_SpeechPhraseElement
	DISPID_SPERetainedStreamOffset=5          # from enum DISPID_SpeechPhraseElement
	DISPID_SPEsCount              =1          # from enum DISPID_SpeechPhraseElements
	DISPID_SPEsItem               =0          # from enum DISPID_SpeechPhraseElements
	DISPID_SPEs_NewEnum           =-4         # from enum DISPID_SpeechPhraseElements
	DISPID_SPIAudioSizeBytes      =5          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIAudioSizeTime       =7          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIAudioStreamPosition =4          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIElements            =10         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIEngineId            =12         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIEnginePrivateData   =13         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIGetDisplayAttributes=16         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIGetText             =15         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIGrammarId           =2          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPILanguageId          =1          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIProperties          =9          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIReplacements        =11         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIRetainedSizeBytes   =6          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIRule                =8          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPISaveToMemory        =14         # from enum DISPID_SpeechPhraseInfo
	DISPID_SPIStartTime           =3          # from enum DISPID_SpeechPhraseInfo
	DISPID_SPPsCount              =1          # from enum DISPID_SpeechPhraseProperties
	DISPID_SPPsItem               =0          # from enum DISPID_SpeechPhraseProperties
	DISPID_SPPs_NewEnum           =-4         # from enum DISPID_SpeechPhraseProperties
	DISPID_SPPChildren            =9          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPConfidence          =7          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPEngineConfidence    =6          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPFirstElement        =4          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPId                  =2          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPName                =1          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPNumberOfElements    =5          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPParent              =8          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPPValue               =3          # from enum DISPID_SpeechPhraseProperty
	DISPID_SPRDisplayAttributes   =1          # from enum DISPID_SpeechPhraseReplacement
	DISPID_SPRFirstElement        =3          # from enum DISPID_SpeechPhraseReplacement
	DISPID_SPRNumberOfElements    =4          # from enum DISPID_SpeechPhraseReplacement
	DISPID_SPRText                =2          # from enum DISPID_SpeechPhraseReplacement
	DISPID_SPRsCount              =1          # from enum DISPID_SpeechPhraseReplacements
	DISPID_SPRsItem               =0          # from enum DISPID_SpeechPhraseReplacements
	DISPID_SPRs_NewEnum           =-4         # from enum DISPID_SpeechPhraseReplacements
	DISPID_SPRuleChildren         =6          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleConfidence       =7          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleEngineConfidence =8          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleFirstElement     =3          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleId               =2          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleName             =1          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleNumberOfElements =4          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRuleParent           =5          # from enum DISPID_SpeechPhraseRule
	DISPID_SPRulesCount           =1          # from enum DISPID_SpeechPhraseRules
	DISPID_SPRulesItem            =0          # from enum DISPID_SpeechPhraseRules
	DISPID_SPRules_NewEnum        =-4         # from enum DISPID_SpeechPhraseRules
	DISPID_SRAllowVoiceFormatMatchingOnNextSet=5          # from enum DISPID_SpeechRecoContext
	DISPID_SRCAudioInInterferenceStatus=2          # from enum DISPID_SpeechRecoContext
	DISPID_SRCBookmark            =16         # from enum DISPID_SpeechRecoContext
	DISPID_SRCCmdMaxAlternates    =8          # from enum DISPID_SpeechRecoContext
	DISPID_SRCCreateGrammar       =14         # from enum DISPID_SpeechRecoContext
	DISPID_SRCCreateResultFromMemory=15         # from enum DISPID_SpeechRecoContext
	DISPID_SRCEventInterests      =7          # from enum DISPID_SpeechRecoContext
	DISPID_SRCPause               =12         # from enum DISPID_SpeechRecoContext
	DISPID_SRCRecognizer          =1          # from enum DISPID_SpeechRecoContext
	DISPID_SRCRequestedUIType     =3          # from enum DISPID_SpeechRecoContext
	DISPID_SRCResume              =13         # from enum DISPID_SpeechRecoContext
	DISPID_SRCRetainedAudio       =10         # from enum DISPID_SpeechRecoContext
	DISPID_SRCRetainedAudioFormat =11         # from enum DISPID_SpeechRecoContext
	DISPID_SRCSetAdaptationData   =17         # from enum DISPID_SpeechRecoContext
	DISPID_SRCState               =9          # from enum DISPID_SpeechRecoContext
	DISPID_SRCVoice               =4          # from enum DISPID_SpeechRecoContext
	DISPID_SRCVoicePurgeEvent     =6          # from enum DISPID_SpeechRecoContext
	DISPID_SRCEAdaptation         =15         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEAudioLevel         =17         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEBookmark           =3          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEEndStream          =2          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEEnginePrivate      =18         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEFalseRecognition   =11         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEHypothesis         =8          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEInterference       =12         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEPhraseStart        =6          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEPropertyNumberChange=9          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEPropertyStringChange=10         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCERecognition        =7          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCERecognitionForOtherContext=16         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCERecognizerStateChange=14         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCERequestUI          =13         # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCESoundEnd           =5          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCESoundStart         =4          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRCEStartStream        =1          # from enum DISPID_SpeechRecoContextEvents
	DISPID_SRRAlternates          =5          # from enum DISPID_SpeechRecoResult
	DISPID_SRRAudio               =6          # from enum DISPID_SpeechRecoResult
	DISPID_SRRAudioFormat         =3          # from enum DISPID_SpeechRecoResult
	DISPID_SRRDiscardResultInfo   =9          # from enum DISPID_SpeechRecoResult
	DISPID_SRRPhraseInfo          =4          # from enum DISPID_SpeechRecoResult
	DISPID_SRRRecoContext         =1          # from enum DISPID_SpeechRecoResult
	DISPID_SRRSaveToMemory        =8          # from enum DISPID_SpeechRecoResult
	DISPID_SRRSpeakAudio          =7          # from enum DISPID_SpeechRecoResult
	DISPID_SRRTimes               =2          # from enum DISPID_SpeechRecoResult
	DISPID_SRRSetTextFeedback     =12         # from enum DISPID_SpeechRecoResult2
	DISPID_SRRTLength             =2          # from enum DISPID_SpeechRecoResultTimes
	DISPID_SRRTOffsetFromStart    =4          # from enum DISPID_SpeechRecoResultTimes
	DISPID_SRRTStreamTime         =1          # from enum DISPID_SpeechRecoResultTimes
	DISPID_SRRTTickCount          =3          # from enum DISPID_SpeechRecoResultTimes
	DISPID_SRAllowAudioInputFormatChangesOnNextSet=2          # from enum DISPID_SpeechRecognizer
	DISPID_SRAudioInput           =3          # from enum DISPID_SpeechRecognizer
	DISPID_SRAudioInputStream     =4          # from enum DISPID_SpeechRecognizer
	DISPID_SRCreateRecoContext    =10         # from enum DISPID_SpeechRecognizer
	DISPID_SRDisplayUI            =17         # from enum DISPID_SpeechRecognizer
	DISPID_SREmulateRecognition   =9          # from enum DISPID_SpeechRecognizer
	DISPID_SRGetFormat            =11         # from enum DISPID_SpeechRecognizer
	DISPID_SRGetPropertyNumber    =13         # from enum DISPID_SpeechRecognizer
	DISPID_SRGetPropertyString    =15         # from enum DISPID_SpeechRecognizer
	DISPID_SRGetRecognizers       =18         # from enum DISPID_SpeechRecognizer
	DISPID_SRIsShared             =5          # from enum DISPID_SpeechRecognizer
	DISPID_SRIsUISupported        =16         # from enum DISPID_SpeechRecognizer
	DISPID_SRProfile              =8          # from enum DISPID_SpeechRecognizer
	DISPID_SRRecognizer           =1          # from enum DISPID_SpeechRecognizer
	DISPID_SRSetPropertyNumber    =12         # from enum DISPID_SpeechRecognizer
	DISPID_SRSetPropertyString    =14         # from enum DISPID_SpeechRecognizer
	DISPID_SRState                =6          # from enum DISPID_SpeechRecognizer
	DISPID_SRStatus               =7          # from enum DISPID_SpeechRecognizer
	DISPID_SVGetAudioInputs       =19         # from enum DISPID_SpeechRecognizer
	DISPID_SVGetProfiles          =20         # from enum DISPID_SpeechRecognizer
	DISPID_SRSAudioStatus         =1          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSClsidEngine         =5          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSCurrentStreamNumber =3          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSCurrentStreamPosition=2          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSNumberOfActiveRules =4          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SRSSupportedLanguages  =6          # from enum DISPID_SpeechRecognizerStatus
	DISPID_SVAlertBoundary        =10         # from enum DISPID_SpeechVoice
	DISPID_SVAllowAudioOuputFormatChangesOnNextSet=7          # from enum DISPID_SpeechVoice
	DISPID_SVAudioOutput          =3          # from enum DISPID_SpeechVoice
	DISPID_SVAudioOutputStream    =4          # from enum DISPID_SpeechVoice
	DISPID_SVDisplayUI            =22         # from enum DISPID_SpeechVoice
	DISPID_SVEventInterests       =8          # from enum DISPID_SpeechVoice
	DISPID_SVGetAudioOutputs      =18         # from enum DISPID_SpeechVoice
	DISPID_SVGetVoices            =17         # from enum DISPID_SpeechVoice
	DISPID_SVIsUISupported        =21         # from enum DISPID_SpeechVoice
	DISPID_SVPause                =14         # from enum DISPID_SpeechVoice
	DISPID_SVPriority             =9          # from enum DISPID_SpeechVoice
	DISPID_SVRate                 =5          # from enum DISPID_SpeechVoice
	DISPID_SVResume               =15         # from enum DISPID_SpeechVoice
	DISPID_SVSkip                 =16         # from enum DISPID_SpeechVoice
	DISPID_SVSpeak                =12         # from enum DISPID_SpeechVoice
	DISPID_SVSpeakCompleteEvent   =20         # from enum DISPID_SpeechVoice
	DISPID_SVSpeakStream          =13         # from enum DISPID_SpeechVoice
	DISPID_SVStatus               =1          # from enum DISPID_SpeechVoice
	DISPID_SVSyncronousSpeakTimeout=11         # from enum DISPID_SpeechVoice
	DISPID_SVVoice                =2          # from enum DISPID_SpeechVoice
	DISPID_SVVolume               =6          # from enum DISPID_SpeechVoice
	DISPID_SVWaitUntilDone        =19         # from enum DISPID_SpeechVoice
	DISPID_SVEAudioLevel          =9          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEBookmark            =4          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEEnginePrivate       =10         # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEPhoneme             =6          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVESentenceBoundary    =7          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEStreamEnd           =2          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEStreamStart         =1          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEViseme              =8          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEVoiceChange         =3          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVEWord                =5          # from enum DISPID_SpeechVoiceEvent
	DISPID_SVSCurrentStreamNumber =1          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSInputSentenceLength =8          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSInputSentencePosition=7          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSInputWordLength     =6          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSInputWordPosition   =5          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSLastBookmark        =9          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSLastBookmarkId      =10         # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSLastResult          =3          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSLastStreamNumberQueued=2          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSPhonemeId           =11         # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSRunningState        =4          # from enum DISPID_SpeechVoiceStatus
	DISPID_SVSVisemeId            =12         # from enum DISPID_SpeechVoiceStatus
	DISPID_SWFEAvgBytesPerSec     =4          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEBitsPerSample      =6          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEBlockAlign         =5          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEChannels           =2          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEExtraData          =7          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFEFormatTag          =1          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SWFESamplesPerSec      =3          # from enum DISPID_SpeechWaveFormatEx
	DISPID_SRRGetXMLErrorInfo     =11         # from enum DISPID_SpeechXMLRecoResult
	DISPID_SRRGetXMLResult        =10         # from enum DISPID_SpeechXMLRecoResult
	SPAR_High                     =3          # from enum SPADAPTATIONRELEVANCE
	SPAR_Low                      =1          # from enum SPADAPTATIONRELEVANCE
	SPAR_Medium                   =2          # from enum SPADAPTATIONRELEVANCE
	SPAR_Unknown                  =0          # from enum SPADAPTATIONRELEVANCE
	SPAO_NONE                     =0          # from enum SPAUDIOOPTIONS
	SPAO_RETAIN_AUDIO             =1          # from enum SPAUDIOOPTIONS
	SPBO_AHEAD                    =2          # from enum SPBOOKMARKOPTIONS
	SPBO_NONE                     =0          # from enum SPBOOKMARKOPTIONS
	SPBO_PAUSE                    =1          # from enum SPBOOKMARKOPTIONS
	SPBO_TIME_UNITS               =4          # from enum SPBOOKMARKOPTIONS
	SPCT_COMMAND                  =0          # from enum SPCATEGORYTYPE
	SPCT_DICTATION                =1          # from enum SPCATEGORYTYPE
	SPCT_SLEEP                    =2          # from enum SPCATEGORYTYPE
	SPCT_SUB_COMMAND              =3          # from enum SPCATEGORYTYPE
	SPCT_SUB_DICTATION            =4          # from enum SPCATEGORYTYPE
	SPCS_DISABLED                 =0          # from enum SPCONTEXTSTATE
	SPCS_ENABLED                  =1          # from enum SPCONTEXTSTATE
	SPDKL_CurrentConfig           =5          # from enum SPDATAKEYLOCATION
	SPDKL_CurrentUser             =1          # from enum SPDATAKEYLOCATION
	SPDKL_DefaultLocation         =0          # from enum SPDATAKEYLOCATION
	SPDKL_LocalMachine            =2          # from enum SPDATAKEYLOCATION
	SPEI_ACTIVE_CATEGORY_CHANGED  =53         # from enum SPEVENTENUM
	SPEI_ADAPTATION               =47         # from enum SPEVENTENUM
	SPEI_END_INPUT_STREAM         =2          # from enum SPEVENTENUM
	SPEI_END_SR_STREAM            =34         # from enum SPEVENTENUM
	SPEI_FALSE_RECOGNITION        =43         # from enum SPEVENTENUM
	SPEI_HYPOTHESIS               =39         # from enum SPEVENTENUM
	SPEI_INTERFERENCE             =44         # from enum SPEVENTENUM
	SPEI_MAX_SR                   =55         # from enum SPEVENTENUM
	SPEI_MAX_TTS                  =15         # from enum SPEVENTENUM
	SPEI_MIN_SR                   =34         # from enum SPEVENTENUM
	SPEI_MIN_TTS                  =1          # from enum SPEVENTENUM
	SPEI_PHONEME                  =6          # from enum SPEVENTENUM
	SPEI_PHRASE_START             =37         # from enum SPEVENTENUM
	SPEI_PROPERTY_NUM_CHANGE      =41         # from enum SPEVENTENUM
	SPEI_PROPERTY_STRING_CHANGE   =42         # from enum SPEVENTENUM
	SPEI_RECOGNITION              =38         # from enum SPEVENTENUM
	SPEI_RECO_OTHER_CONTEXT       =49         # from enum SPEVENTENUM
	SPEI_RECO_STATE_CHANGE        =46         # from enum SPEVENTENUM
	SPEI_REQUEST_UI               =45         # from enum SPEVENTENUM
	SPEI_RESERVED1                =30         # from enum SPEVENTENUM
	SPEI_RESERVED2                =33         # from enum SPEVENTENUM
	SPEI_RESERVED3                =63         # from enum SPEVENTENUM
	SPEI_RESERVED5                =54         # from enum SPEVENTENUM
	SPEI_RESERVED6                =55         # from enum SPEVENTENUM
	SPEI_SENTENCE_BOUNDARY        =7          # from enum SPEVENTENUM
	SPEI_SOUND_END                =36         # from enum SPEVENTENUM
	SPEI_SOUND_START              =35         # from enum SPEVENTENUM
	SPEI_SR_AUDIO_LEVEL           =50         # from enum SPEVENTENUM
	SPEI_SR_BOOKMARK              =40         # from enum SPEVENTENUM
	SPEI_SR_PRIVATE               =52         # from enum SPEVENTENUM
	SPEI_SR_RETAINEDAUDIO         =51         # from enum SPEVENTENUM
	SPEI_START_INPUT_STREAM       =1          # from enum SPEVENTENUM
	SPEI_START_SR_STREAM          =48         # from enum SPEVENTENUM
	SPEI_TTS_AUDIO_LEVEL          =9          # from enum SPEVENTENUM
	SPEI_TTS_BOOKMARK             =4          # from enum SPEVENTENUM
	SPEI_TTS_PRIVATE              =15         # from enum SPEVENTENUM
	SPEI_UNDEFINED                =0          # from enum SPEVENTENUM
	SPEI_VISEME                   =8          # from enum SPEVENTENUM
	SPEI_VOICE_CHANGE             =3          # from enum SPEVENTENUM
	SPEI_WORD_BOUNDARY            =5          # from enum SPEVENTENUM
	SPFM_CREATE                   =2          # from enum SPFILEMODE
	SPFM_CREATE_ALWAYS            =3          # from enum SPFILEMODE
	SPFM_NUM_MODES                =4          # from enum SPFILEMODE
	SPFM_OPEN_READONLY            =0          # from enum SPFILEMODE
	SPFM_OPEN_READWRITE           =1          # from enum SPFILEMODE
	SPGS_DISABLED                 =0          # from enum SPGRAMMARSTATE
	SPGS_ENABLED                  =1          # from enum SPGRAMMARSTATE
	SPGS_EXCLUSIVE                =3          # from enum SPGRAMMARSTATE
	SPWT_DISPLAY                  =0          # from enum SPGRAMMARWORDTYPE
	SPWT_LEXICAL                  =1          # from enum SPGRAMMARWORDTYPE
	SPWT_LEXICAL_NO_SPECIAL_CHARS =3          # from enum SPGRAMMARWORDTYPE
	SPWT_PRONUNCIATION            =2          # from enum SPGRAMMARWORDTYPE
	SPINTERFERENCE_NOISE          =1          # from enum SPINTERFERENCE
	SPINTERFERENCE_NONE           =0          # from enum SPINTERFERENCE
	SPINTERFERENCE_NOSIGNAL       =2          # from enum SPINTERFERENCE
	SPINTERFERENCE_TOOFAST        =5          # from enum SPINTERFERENCE
	SPINTERFERENCE_TOOLOUD        =3          # from enum SPINTERFERENCE
	SPINTERFERENCE_TOOQUIET       =4          # from enum SPINTERFERENCE
	SPINTERFERENCE_TOOSLOW        =6          # from enum SPINTERFERENCE
	eLEXTYPE_APP                  =2          # from enum SPLEXICONTYPE
	eLEXTYPE_LETTERTOSOUND        =8          # from enum SPLEXICONTYPE
	eLEXTYPE_MORPHOLOGY           =16         # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE1             =4096       # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE10            =2097152    # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE11            =4194304    # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE12            =8388608    # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE13            =16777216   # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE14            =33554432   # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE15            =67108864   # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE16            =134217728  # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE17            =268435456  # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE18            =536870912  # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE19            =1073741824 # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE2             =8192       # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE20            =-2147483648 # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE3             =16384      # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE4             =32768      # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE5             =65536      # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE6             =131072     # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE7             =262144     # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE8             =524288     # from enum SPLEXICONTYPE
	eLEXTYPE_PRIVATE9             =1048576    # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED10           =2048       # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED4            =32         # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED6            =128        # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED7            =256        # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED8            =512        # from enum SPLEXICONTYPE
	eLEXTYPE_RESERVED9            =1024       # from enum SPLEXICONTYPE
	eLEXTYPE_USER                 =1          # from enum SPLEXICONTYPE
	eLEXTYPE_USER_SHORTCUT        =64         # from enum SPLEXICONTYPE
	eLEXTYPE_VENDORLEXICON        =4          # from enum SPLEXICONTYPE
	SPLO_DYNAMIC                  =1          # from enum SPLOADOPTIONS
	SPLO_STATIC                   =0          # from enum SPLOADOPTIONS
	SPPS_Function                 =16384      # from enum SPPARTOFSPEECH
	SPPS_Interjection             =20480      # from enum SPPARTOFSPEECH
	SPPS_LMA                      =28672      # from enum SPPARTOFSPEECH
	SPPS_Modifier                 =12288      # from enum SPPARTOFSPEECH
	SPPS_Noncontent               =24576      # from enum SPPARTOFSPEECH
	SPPS_NotOverriden             =-1         # from enum SPPARTOFSPEECH
	SPPS_Noun                     =4096       # from enum SPPARTOFSPEECH
	SPPS_SuppressWord             =61440      # from enum SPPARTOFSPEECH
	SPPS_Unknown                  =0          # from enum SPPARTOFSPEECH
	SPPS_Verb                     =8192       # from enum SPPARTOFSPEECH
	SPRST_ACTIVE                  =1          # from enum SPRECOSTATE
	SPRST_ACTIVE_ALWAYS           =2          # from enum SPRECOSTATE
	SPRST_INACTIVE                =0          # from enum SPRECOSTATE
	SPRST_INACTIVE_WITH_PURGE     =3          # from enum SPRECOSTATE
	SPRST_NUM_STATES              =4          # from enum SPRECOSTATE
	SPRS_ACTIVE                   =1          # from enum SPRULESTATE
	SPRS_ACTIVE_USER_DELIMITED    =4          # from enum SPRULESTATE
	SPRS_ACTIVE_WITH_AUTO_PAUSE   =3          # from enum SPRULESTATE
	SPRS_INACTIVE                 =0          # from enum SPRULESTATE
	SPSMF_SAPI_PROPERTIES         =0          # from enum SPSEMANTICFORMAT
	SPSMF_SRGS_SAPIPROPERTIES     =2          # from enum SPSEMANTICFORMAT
	SPSMF_SRGS_SEMANTICINTERPRETATION_MS=1          # from enum SPSEMANTICFORMAT
	SPSMF_SRGS_SEMANTICINTERPRETATION_W3C=8          # from enum SPSEMANTICFORMAT
	SPSMF_UPS                     =4          # from enum SPSEMANTICFORMAT
	SPPS_RESERVED1                =12288      # from enum SPSHORTCUTTYPE
	SPPS_RESERVED2                =16384      # from enum SPSHORTCUTTYPE
	SPPS_RESERVED3                =20480      # from enum SPSHORTCUTTYPE
	SPPS_RESERVED4                =61440      # from enum SPSHORTCUTTYPE
	SPSHT_EMAIL                   =4096       # from enum SPSHORTCUTTYPE
	SPSHT_NotOverriden            =-1         # from enum SPSHORTCUTTYPE
	SPSHT_OTHER                   =8192       # from enum SPSHORTCUTTYPE
	SPSHT_Unknown                 =0          # from enum SPSHORTCUTTYPE
	SP_VISEME_0                   =0          # from enum SPVISEMES
	SP_VISEME_1                   =1          # from enum SPVISEMES
	SP_VISEME_10                  =10         # from enum SPVISEMES
	SP_VISEME_11                  =11         # from enum SPVISEMES
	SP_VISEME_12                  =12         # from enum SPVISEMES
	SP_VISEME_13                  =13         # from enum SPVISEMES
	SP_VISEME_14                  =14         # from enum SPVISEMES
	SP_VISEME_15                  =15         # from enum SPVISEMES
	SP_VISEME_16                  =16         # from enum SPVISEMES
	SP_VISEME_17                  =17         # from enum SPVISEMES
	SP_VISEME_18                  =18         # from enum SPVISEMES
	SP_VISEME_19                  =19         # from enum SPVISEMES
	SP_VISEME_2                   =2          # from enum SPVISEMES
	SP_VISEME_20                  =20         # from enum SPVISEMES
	SP_VISEME_21                  =21         # from enum SPVISEMES
	SP_VISEME_3                   =3          # from enum SPVISEMES
	SP_VISEME_4                   =4          # from enum SPVISEMES
	SP_VISEME_5                   =5          # from enum SPVISEMES
	SP_VISEME_6                   =6          # from enum SPVISEMES
	SP_VISEME_7                   =7          # from enum SPVISEMES
	SP_VISEME_8                   =8          # from enum SPVISEMES
	SP_VISEME_9                   =9          # from enum SPVISEMES
	SPVPRI_ALERT                  =1          # from enum SPVPRIORITY
	SPVPRI_NORMAL                 =0          # from enum SPVPRIORITY
	SPVPRI_OVER                   =2          # from enum SPVPRIORITY
	SPWF_INPUT                    =0          # from enum SPWAVEFORMATTYPE
	SPWF_SRENGINE                 =1          # from enum SPWAVEFORMATTYPE
	SPWP_KNOWN_WORD_PRONOUNCEABLE =2          # from enum SPWORDPRONOUNCEABLE
	SPWP_UNKNOWN_WORD_PRONOUNCEABLE=1          # from enum SPWORDPRONOUNCEABLE
	SPWP_UNKNOWN_WORD_UNPRONOUNCEABLE=0          # from enum SPWORDPRONOUNCEABLE
	eWORDTYPE_ADDED               =1          # from enum SPWORDTYPE
	eWORDTYPE_DELETED             =2          # from enum SPWORDTYPE
	SPXRO_Alternates_SML          =1          # from enum SPXMLRESULTOPTIONS
	SPXRO_SML                     =0          # from enum SPXMLRESULTOPTIONS
	SAFT11kHz16BitMono            =10         # from enum SpeechAudioFormatType
	SAFT11kHz16BitStereo          =11         # from enum SpeechAudioFormatType
	SAFT11kHz8BitMono             =8          # from enum SpeechAudioFormatType
	SAFT11kHz8BitStereo           =9          # from enum SpeechAudioFormatType
	SAFT12kHz16BitMono            =14         # from enum SpeechAudioFormatType
	SAFT12kHz16BitStereo          =15         # from enum SpeechAudioFormatType
	SAFT12kHz8BitMono             =12         # from enum SpeechAudioFormatType
	SAFT12kHz8BitStereo           =13         # from enum SpeechAudioFormatType
	SAFT16kHz16BitMono            =18         # from enum SpeechAudioFormatType
	SAFT16kHz16BitStereo          =19         # from enum SpeechAudioFormatType
	SAFT16kHz8BitMono             =16         # from enum SpeechAudioFormatType
	SAFT16kHz8BitStereo           =17         # from enum SpeechAudioFormatType
	SAFT22kHz16BitMono            =22         # from enum SpeechAudioFormatType
	SAFT22kHz16BitStereo          =23         # from enum SpeechAudioFormatType
	SAFT22kHz8BitMono             =20         # from enum SpeechAudioFormatType
	SAFT22kHz8BitStereo           =21         # from enum SpeechAudioFormatType
	SAFT24kHz16BitMono            =26         # from enum SpeechAudioFormatType
	SAFT24kHz16BitStereo          =27         # from enum SpeechAudioFormatType
	SAFT24kHz8BitMono             =24         # from enum SpeechAudioFormatType
	SAFT24kHz8BitStereo           =25         # from enum SpeechAudioFormatType
	SAFT32kHz16BitMono            =30         # from enum SpeechAudioFormatType
	SAFT32kHz16BitStereo          =31         # from enum SpeechAudioFormatType
	SAFT32kHz8BitMono             =28         # from enum SpeechAudioFormatType
	SAFT32kHz8BitStereo           =29         # from enum SpeechAudioFormatType
	SAFT44kHz16BitMono            =34         # from enum SpeechAudioFormatType
	SAFT44kHz16BitStereo          =35         # from enum SpeechAudioFormatType
	SAFT44kHz8BitMono             =32         # from enum SpeechAudioFormatType
	SAFT44kHz8BitStereo           =33         # from enum SpeechAudioFormatType
	SAFT48kHz16BitMono            =38         # from enum SpeechAudioFormatType
	SAFT48kHz16BitStereo          =39         # from enum SpeechAudioFormatType
	SAFT48kHz8BitMono             =36         # from enum SpeechAudioFormatType
	SAFT48kHz8BitStereo           =37         # from enum SpeechAudioFormatType
	SAFT8kHz16BitMono             =6          # from enum SpeechAudioFormatType
	SAFT8kHz16BitStereo           =7          # from enum SpeechAudioFormatType
	SAFT8kHz8BitMono              =4          # from enum SpeechAudioFormatType
	SAFT8kHz8BitStereo            =5          # from enum SpeechAudioFormatType
	SAFTADPCM_11kHzMono           =59         # from enum SpeechAudioFormatType
	SAFTADPCM_11kHzStereo         =60         # from enum SpeechAudioFormatType
	SAFTADPCM_22kHzMono           =61         # from enum SpeechAudioFormatType
	SAFTADPCM_22kHzStereo         =62         # from enum SpeechAudioFormatType
	SAFTADPCM_44kHzMono           =63         # from enum SpeechAudioFormatType
	SAFTADPCM_44kHzStereo         =64         # from enum SpeechAudioFormatType
	SAFTADPCM_8kHzMono            =57         # from enum SpeechAudioFormatType
	SAFTADPCM_8kHzStereo          =58         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_11kHzMono      =43         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_11kHzStereo    =44         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_22kHzMono      =45         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_22kHzStereo    =46         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_44kHzMono      =47         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_44kHzStereo    =48         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_8kHzMono       =41         # from enum SpeechAudioFormatType
	SAFTCCITT_ALaw_8kHzStereo     =42         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_11kHzMono      =51         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_11kHzStereo    =52         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_22kHzMono      =53         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_22kHzStereo    =54         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_44kHzMono      =55         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_44kHzStereo    =56         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_8kHzMono       =49         # from enum SpeechAudioFormatType
	SAFTCCITT_uLaw_8kHzStereo     =50         # from enum SpeechAudioFormatType
	SAFTDefault                   =-1         # from enum SpeechAudioFormatType
	SAFTExtendedAudioFormat       =3          # from enum SpeechAudioFormatType
	SAFTGSM610_11kHzMono          =66         # from enum SpeechAudioFormatType
	SAFTGSM610_22kHzMono          =67         # from enum SpeechAudioFormatType
	SAFTGSM610_44kHzMono          =68         # from enum SpeechAudioFormatType
	SAFTGSM610_8kHzMono           =65         # from enum SpeechAudioFormatType
	SAFTNoAssignedFormat          =0          # from enum SpeechAudioFormatType
	SAFTNonStandardFormat         =2          # from enum SpeechAudioFormatType
	SAFTText                      =1          # from enum SpeechAudioFormatType
	SAFTTrueSpeech_8kHz1BitMono   =40         # from enum SpeechAudioFormatType
	SASClosed                     =0          # from enum SpeechAudioState
	SASPause                      =2          # from enum SpeechAudioState
	SASRun                        =3          # from enum SpeechAudioState
	SASStop                       =1          # from enum SpeechAudioState
	SBONone                       =0          # from enum SpeechBookmarkOptions
	SBOPause                      =1          # from enum SpeechBookmarkOptions
	SpeechAllElements             =-1         # from enum SpeechConstants
	Speech_Default_Weight         =1.0        # from enum SpeechConstants
	Speech_Max_Pron_Length        =384        # from enum SpeechConstants
	Speech_Max_Word_Length        =128        # from enum SpeechConstants
	Speech_StreamPos_Asap         =0          # from enum SpeechConstants
	Speech_StreamPos_RealTime     =-1         # from enum SpeechConstants
	SDKLCurrentConfig             =5          # from enum SpeechDataKeyLocation
	SDKLCurrentUser               =1          # from enum SpeechDataKeyLocation
	SDKLDefaultLocation           =0          # from enum SpeechDataKeyLocation
	SDKLLocalMachine              =2          # from enum SpeechDataKeyLocation
	SDTAll                        =255        # from enum SpeechDiscardType
	SDTAlternates                 =128        # from enum SpeechDiscardType
	SDTAudio                      =64         # from enum SpeechDiscardType
	SDTDisplayText                =8          # from enum SpeechDiscardType
	SDTLexicalForm                =16         # from enum SpeechDiscardType
	SDTPronunciation              =32         # from enum SpeechDiscardType
	SDTProperty                   =1          # from enum SpeechDiscardType
	SDTReplacement                =2          # from enum SpeechDiscardType
	SDTRule                       =4          # from enum SpeechDiscardType
	SDA_Consume_Leading_Spaces    =8          # from enum SpeechDisplayAttributes
	SDA_No_Trailing_Space         =0          # from enum SpeechDisplayAttributes
	SDA_One_Trailing_Space        =2          # from enum SpeechDisplayAttributes
	SDA_Two_Trailing_Spaces       =4          # from enum SpeechDisplayAttributes
	SECFDefault                   =196609     # from enum SpeechEmulationCompareFlags
	SECFEmulateResult             =1073741824 # from enum SpeechEmulationCompareFlags
	SECFIgnoreCase                =1          # from enum SpeechEmulationCompareFlags
	SECFIgnoreKanaType            =65536      # from enum SpeechEmulationCompareFlags
	SECFIgnoreWidth               =131072     # from enum SpeechEmulationCompareFlags
	SECFNoSpecialChars            =536870912  # from enum SpeechEmulationCompareFlags
	SECHighConfidence             =1          # from enum SpeechEngineConfidence
	SECLowConfidence              =-1         # from enum SpeechEngineConfidence
	SECNormalConfidence           =0          # from enum SpeechEngineConfidence
	SFTInput                      =0          # from enum SpeechFormatType
	SFTSREngine                   =1          # from enum SpeechFormatType
	SGRSTTDictation               =3          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTEpsilon                 =0          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTRule                    =2          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTTextBuffer              =5          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTWildcard                =4          # from enum SpeechGrammarRuleStateTransitionType
	SGRSTTWord                    =1          # from enum SpeechGrammarRuleStateTransitionType
	SGSDisabled                   =0          # from enum SpeechGrammarState
	SGSEnabled                    =1          # from enum SpeechGrammarState
	SGSExclusive                  =3          # from enum SpeechGrammarState
	SGDisplay                     =0          # from enum SpeechGrammarWordType
	SGLexical                     =1          # from enum SpeechGrammarWordType
	SGLexicalNoSpecialChars       =3          # from enum SpeechGrammarWordType
	SGPronounciation              =2          # from enum SpeechGrammarWordType
	SINoSignal                    =2          # from enum SpeechInterference
	SINoise                       =1          # from enum SpeechInterference
	SINone                        =0          # from enum SpeechInterference
	SITooFast                     =5          # from enum SpeechInterference
	SITooLoud                     =3          # from enum SpeechInterference
	SITooQuiet                    =4          # from enum SpeechInterference
	SITooSlow                     =6          # from enum SpeechInterference
	SLTApp                        =2          # from enum SpeechLexiconType
	SLTUser                       =1          # from enum SpeechLexiconType
	SLODynamic                    =1          # from enum SpeechLoadOption
	SLOStatic                     =0          # from enum SpeechLoadOption
	SPSFunction                   =16384      # from enum SpeechPartOfSpeech
	SPSInterjection               =20480      # from enum SpeechPartOfSpeech
	SPSLMA                        =28672      # from enum SpeechPartOfSpeech
	SPSModifier                   =12288      # from enum SpeechPartOfSpeech
	SPSNotOverriden               =-1         # from enum SpeechPartOfSpeech
	SPSNoun                       =4096       # from enum SpeechPartOfSpeech
	SPSSuppressWord               =61440      # from enum SpeechPartOfSpeech
	SPSUnknown                    =0          # from enum SpeechPartOfSpeech
	SPSVerb                       =8192       # from enum SpeechPartOfSpeech
	SRCS_Disabled                 =0          # from enum SpeechRecoContextState
	SRCS_Enabled                  =1          # from enum SpeechRecoContextState
	SREAdaptation                 =8192       # from enum SpeechRecoEvents
	SREAllEvents                  =393215     # from enum SpeechRecoEvents
	SREAudioLevel                 =65536      # from enum SpeechRecoEvents
	SREBookmark                   =64         # from enum SpeechRecoEvents
	SREFalseRecognition           =512        # from enum SpeechRecoEvents
	SREHypothesis                 =32         # from enum SpeechRecoEvents
	SREInterference               =1024       # from enum SpeechRecoEvents
	SREPhraseStart                =8          # from enum SpeechRecoEvents
	SREPrivate                    =262144     # from enum SpeechRecoEvents
	SREPropertyNumChange          =128        # from enum SpeechRecoEvents
	SREPropertyStringChange       =256        # from enum SpeechRecoEvents
	SRERecoOtherContext           =32768      # from enum SpeechRecoEvents
	SRERecognition                =16         # from enum SpeechRecoEvents
	SRERequestUI                  =2048       # from enum SpeechRecoEvents
	SRESoundEnd                   =4          # from enum SpeechRecoEvents
	SRESoundStart                 =2          # from enum SpeechRecoEvents
	SREStateChange                =4096       # from enum SpeechRecoEvents
	SREStreamEnd                  =1          # from enum SpeechRecoEvents
	SREStreamStart                =16384      # from enum SpeechRecoEvents
	SRTAutopause                  =1          # from enum SpeechRecognitionType
	SRTEmulated                   =2          # from enum SpeechRecognitionType
	SRTExtendableParse            =8          # from enum SpeechRecognitionType
	SRTReSent                     =16         # from enum SpeechRecognitionType
	SRTSMLTimeout                 =4          # from enum SpeechRecognitionType
	SRTStandard                   =0          # from enum SpeechRecognitionType
	SRSActive                     =1          # from enum SpeechRecognizerState
	SRSActiveAlways               =2          # from enum SpeechRecognizerState
	SRSInactive                   =0          # from enum SpeechRecognizerState
	SRSInactiveWithPurge          =3          # from enum SpeechRecognizerState
	SRAONone                      =0          # from enum SpeechRetainedAudioOptions
	SRAORetainAudio               =1          # from enum SpeechRetainedAudioOptions
	SRADefaultToActive            =2          # from enum SpeechRuleAttributes
	SRADynamic                    =32         # from enum SpeechRuleAttributes
	SRAExport                     =4          # from enum SpeechRuleAttributes
	SRAImport                     =8          # from enum SpeechRuleAttributes
	SRAInterpreter                =16         # from enum SpeechRuleAttributes
	SRARoot                       =64         # from enum SpeechRuleAttributes
	SRATopLevel                   =1          # from enum SpeechRuleAttributes
	SGDSActive                    =1          # from enum SpeechRuleState
	SGDSActiveUserDelimited       =4          # from enum SpeechRuleState
	SGDSActiveWithAutoPause       =3          # from enum SpeechRuleState
	SGDSInactive                  =0          # from enum SpeechRuleState
	SRSEDone                      =1          # from enum SpeechRunState
	SRSEIsSpeaking                =2          # from enum SpeechRunState
	SSTTDictation                 =2          # from enum SpeechSpecialTransitionType
	SSTTTextBuffer                =3          # from enum SpeechSpecialTransitionType
	SSTTWildcard                  =1          # from enum SpeechSpecialTransitionType
	SSFMCreate                    =2          # from enum SpeechStreamFileMode
	SSFMCreateForWrite            =3          # from enum SpeechStreamFileMode
	SSFMOpenForRead               =0          # from enum SpeechStreamFileMode
	SSFMOpenReadWrite             =1          # from enum SpeechStreamFileMode
	SSSPTRelativeToCurrentPosition=1          # from enum SpeechStreamSeekPositionType
	SSSPTRelativeToEnd            =2          # from enum SpeechStreamSeekPositionType
	SSSPTRelativeToStart          =0          # from enum SpeechStreamSeekPositionType
	SpeechAddRemoveWord           =u'AddRemoveWord' # from enum SpeechStringConstants
	SpeechAudioFormatGUIDText     =u'{7CEEF9F9-3D13-11d2-9EE7-00C04F797396}' # from enum SpeechStringConstants
	SpeechAudioFormatGUIDWave     =u'{C31ADBAE-527F-4ff5-A230-F62BB61FF70C}' # from enum SpeechStringConstants
	SpeechAudioProperties         =u'AudioProperties' # from enum SpeechStringConstants
	SpeechAudioVolume             =u'AudioVolume' # from enum SpeechStringConstants
	SpeechCategoryAppLexicons     =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AppLexicons' # from enum SpeechStringConstants
	SpeechCategoryAudioIn         =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AudioInput' # from enum SpeechStringConstants
	SpeechCategoryAudioOut        =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\AudioOutput' # from enum SpeechStringConstants
	SpeechCategoryPhoneConverters =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\PhoneConverters' # from enum SpeechStringConstants
	SpeechCategoryRecoProfiles    =u'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech\\RecoProfiles' # from enum SpeechStringConstants
	SpeechCategoryRecognizers     =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Recognizers' # from enum SpeechStringConstants
	SpeechCategoryVoices          =u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices' # from enum SpeechStringConstants
	SpeechDictationTopicSpelling  =u'Spelling' # from enum SpeechStringConstants
	SpeechEngineProperties        =u'EngineProperties' # from enum SpeechStringConstants
	SpeechGrammarTagDictation     =u'*'       # from enum SpeechStringConstants
	SpeechGrammarTagUnlimitedDictation=u'*+'      # from enum SpeechStringConstants
	SpeechGrammarTagWildcard      =u'...'     # from enum SpeechStringConstants
	SpeechMicTraining             =u'MicTraining' # from enum SpeechStringConstants
	SpeechPropertyAdaptationOn    =u'AdaptationOn' # from enum SpeechStringConstants
	SpeechPropertyComplexResponseSpeed=u'ComplexResponseSpeed' # from enum SpeechStringConstants
	SpeechPropertyHighConfidenceThreshold=u'HighConfidenceThreshold' # from enum SpeechStringConstants
	SpeechPropertyLowConfidenceThreshold=u'LowConfidenceThreshold' # from enum SpeechStringConstants
	SpeechPropertyNormalConfidenceThreshold=u'NormalConfidenceThreshold' # from enum SpeechStringConstants
	SpeechPropertyResourceUsage   =u'ResourceUsage' # from enum SpeechStringConstants
	SpeechPropertyResponseSpeed   =u'ResponseSpeed' # from enum SpeechStringConstants
	SpeechRecoProfileProperties   =u'RecoProfileProperties' # from enum SpeechStringConstants
	SpeechRegistryLocalMachineRoot=u'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech' # from enum SpeechStringConstants
	SpeechRegistryUserRoot        =u'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech' # from enum SpeechStringConstants
	SpeechTokenIdUserLexicon      =u'HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Speech\\CurrentUserLexicon' # from enum SpeechStringConstants
	SpeechTokenKeyAttributes      =u'Attributes' # from enum SpeechStringConstants
	SpeechTokenKeyFiles           =u'Files'   # from enum SpeechStringConstants
	SpeechTokenKeyUI              =u'UI'      # from enum SpeechStringConstants
	SpeechTokenValueCLSID         =u'CLSID'   # from enum SpeechStringConstants
	SpeechUserTraining            =u'UserTraining' # from enum SpeechStringConstants
	SpeechVoiceCategoryTTSRate    =u'DefaultTTSRate' # from enum SpeechStringConstants
	SpeechVoiceSkipTypeSentence   =u'Sentence' # from enum SpeechStringConstants
	STCAll                        =23         # from enum SpeechTokenContext
	STCInprocHandler              =2          # from enum SpeechTokenContext
	STCInprocServer               =1          # from enum SpeechTokenContext
	STCLocalServer                =4          # from enum SpeechTokenContext
	STCRemoteServer               =16         # from enum SpeechTokenContext
	STSF_AppData                  =26         # from enum SpeechTokenShellFolder
	STSF_CommonAppData            =35         # from enum SpeechTokenShellFolder
	STSF_FlagCreate               =32768      # from enum SpeechTokenShellFolder
	STSF_LocalAppData             =28         # from enum SpeechTokenShellFolder
	SVF_Emphasis                  =2          # from enum SpeechVisemeFeature
	SVF_None                      =0          # from enum SpeechVisemeFeature
	SVF_Stressed                  =1          # from enum SpeechVisemeFeature
	SVP_0                         =0          # from enum SpeechVisemeType
	SVP_1                         =1          # from enum SpeechVisemeType
	SVP_10                        =10         # from enum SpeechVisemeType
	SVP_11                        =11         # from enum SpeechVisemeType
	SVP_12                        =12         # from enum SpeechVisemeType
	SVP_13                        =13         # from enum SpeechVisemeType
	SVP_14                        =14         # from enum SpeechVisemeType
	SVP_15                        =15         # from enum SpeechVisemeType
	SVP_16                        =16         # from enum SpeechVisemeType
	SVP_17                        =17         # from enum SpeechVisemeType
	SVP_18                        =18         # from enum SpeechVisemeType
	SVP_19                        =19         # from enum SpeechVisemeType
	SVP_2                         =2          # from enum SpeechVisemeType
	SVP_20                        =20         # from enum SpeechVisemeType
	SVP_21                        =21         # from enum SpeechVisemeType
	SVP_3                         =3          # from enum SpeechVisemeType
	SVP_4                         =4          # from enum SpeechVisemeType
	SVP_5                         =5          # from enum SpeechVisemeType
	SVP_6                         =6          # from enum SpeechVisemeType
	SVP_7                         =7          # from enum SpeechVisemeType
	SVP_8                         =8          # from enum SpeechVisemeType
	SVP_9                         =9          # from enum SpeechVisemeType
	SVEAllEvents                  =33790      # from enum SpeechVoiceEvents
	SVEAudioLevel                 =512        # from enum SpeechVoiceEvents
	SVEBookmark                   =16         # from enum SpeechVoiceEvents
	SVEEndInputStream             =4          # from enum SpeechVoiceEvents
	SVEPhoneme                    =64         # from enum SpeechVoiceEvents
	SVEPrivate                    =32768      # from enum SpeechVoiceEvents
	SVESentenceBoundary           =128        # from enum SpeechVoiceEvents
	SVEStartInputStream           =2          # from enum SpeechVoiceEvents
	SVEViseme                     =256        # from enum SpeechVoiceEvents
	SVEVoiceChange                =8          # from enum SpeechVoiceEvents
	SVEWordBoundary               =32         # from enum SpeechVoiceEvents
	SVPAlert                      =1          # from enum SpeechVoicePriority
	SVPNormal                     =0          # from enum SpeechVoicePriority
	SVPOver                       =2          # from enum SpeechVoicePriority
	SVSFDefault                   =0          # from enum SpeechVoiceSpeakFlags
	SVSFIsFilename                =4          # from enum SpeechVoiceSpeakFlags
	SVSFIsNotXML                  =16         # from enum SpeechVoiceSpeakFlags
	SVSFIsXML                     =8          # from enum SpeechVoiceSpeakFlags
	SVSFNLPMask                   =64         # from enum SpeechVoiceSpeakFlags
	SVSFNLPSpeakPunc              =64         # from enum SpeechVoiceSpeakFlags
	SVSFParseAutodetect           =0          # from enum SpeechVoiceSpeakFlags
	SVSFParseMask                 =384        # from enum SpeechVoiceSpeakFlags
	SVSFParseSapi                 =128        # from enum SpeechVoiceSpeakFlags
	SVSFParseSsml                 =256        # from enum SpeechVoiceSpeakFlags
	SVSFPersistXML                =32         # from enum SpeechVoiceSpeakFlags
	SVSFPurgeBeforeSpeak          =2          # from enum SpeechVoiceSpeakFlags
	SVSFUnusedFlags               =-512       # from enum SpeechVoiceSpeakFlags
	SVSFVoiceMask                 =511        # from enum SpeechVoiceSpeakFlags
	SVSFlagsAsync                 =1          # from enum SpeechVoiceSpeakFlags
	SWPKnownWordPronounceable     =2          # from enum SpeechWordPronounceable
	SWPUnknownWordPronounceable   =1          # from enum SpeechWordPronounceable
	SWPUnknownWordUnpronounceable =0          # from enum SpeechWordPronounceable
	SWTAdded                      =1          # from enum SpeechWordType
	SWTDeleted                    =2          # from enum SpeechWordType
	SPAS_CLOSED                   =0          # from enum _SPAUDIOSTATE
	SPAS_PAUSE                    =2          # from enum _SPAUDIOSTATE
	SPAS_RUN                      =3          # from enum _SPAUDIOSTATE
	SPAS_STOP                     =1          # from enum _SPAUDIOSTATE

from win32com.client import DispatchBaseClass
class ISpeechAudio(DispatchBaseClass):
	'ISpeechAudio Interface'
	CLSID = IID('{CFF8E175-019E-11D3-A08E-00C04F8EF9B5}')
	coclass_clsid = None

	def Read(self, Buffer=pythoncom.Missing, NumberOfBytes=defaultNamedNotOptArg):
		'Read'
		return self._ApplyTypes_(2, 1, (3, 0), ((16396, 2), (3, 1)), u'Read', None,Buffer
			, NumberOfBytes)

	def Seek(self, Position=defaultNamedNotOptArg, Origin=0):
		'Seek'
		return self._ApplyTypes_(4, 1, (12, 0), ((12, 1), (3, 49)), u'Seek', None,Position
			, Origin)

	def SetState(self, State=defaultNamedNotOptArg):
		'SetState'
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), ((3, 1),),State
			)

	def Write(self, Buffer=defaultNamedNotOptArg):
		'Write'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((12, 1),),Buffer
			)

	_prop_map_get_ = {
		# Method 'BufferInfo' returns object of type 'ISpeechAudioBufferInfo'
		"BufferInfo": (201, 2, (9, 0), (), "BufferInfo", '{11B103D8-1142-4EDF-A093-82FB3915F8CC}'),
		"BufferNotifySize": (204, 2, (3, 0), (), "BufferNotifySize", None),
		# Method 'DefaultFormat' returns object of type 'ISpeechAudioFormat'
		"DefaultFormat": (202, 2, (9, 0), (), "DefaultFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		"EventHandle": (205, 2, (3, 0), (), "EventHandle", None),
		# Method 'Format' returns object of type 'ISpeechAudioFormat'
		"Format": (1, 2, (9, 0), (), "Format", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		# Method 'Status' returns object of type 'ISpeechAudioStatus'
		"Status": (200, 2, (9, 0), (), "Status", '{C62D9C91-7458-47F6-862D-1EF86FB0B278}'),
		"Volume": (203, 2, (3, 0), (), "Volume", None),
	}
	_prop_map_put_ = {
		"BufferNotifySize": ((204, LCID, 4, 0),()),
		"Format": ((1, LCID, 8, 0),()),
		"Volume": ((203, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechAudioBufferInfo(DispatchBaseClass):
	'ISpeechAudioBufferInfo Interface'
	CLSID = IID('{11B103D8-1142-4EDF-A093-82FB3915F8CC}')
	coclass_clsid = None

	_prop_map_get_ = {
		"BufferSize": (2, 2, (3, 0), (), "BufferSize", None),
		"EventBias": (3, 2, (3, 0), (), "EventBias", None),
		"MinNotification": (1, 2, (3, 0), (), "MinNotification", None),
	}
	_prop_map_put_ = {
		"BufferSize": ((2, LCID, 4, 0),()),
		"EventBias": ((3, LCID, 4, 0),()),
		"MinNotification": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechAudioFormat(DispatchBaseClass):
	'ISpeechAudioFormat Interface'
	CLSID = IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')
	coclass_clsid = IID('{9EF96870-E160-4792-820D-48CF0649E4EC}')

	# Result is of type ISpeechWaveFormatEx
	def GetWaveFormatEx(self):
		'GetWaveFormatEx'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'GetWaveFormatEx', '{7A1EF0D5-1581-4741-88E4-209A49F11A10}')
		return ret

	def SetWaveFormatEx(self, WaveFormatEx=defaultNamedNotOptArg):
		'SetWaveFormatEx'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), ((9, 1),),WaveFormatEx
			)

	_prop_map_get_ = {
		"Guid": (2, 2, (8, 0), (), "Guid", None),
		"Type": (1, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
		"Guid": ((2, LCID, 4, 0),()),
		"Type": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechAudioStatus(DispatchBaseClass):
	'ISpeechAudioStatus Interface'
	CLSID = IID('{C62D9C91-7458-47F6-862D-1EF86FB0B278}')
	coclass_clsid = None

	_prop_map_get_ = {
		"CurrentDevicePosition": (5, 2, (12, 0), (), "CurrentDevicePosition", None),
		"CurrentSeekPosition": (4, 2, (12, 0), (), "CurrentSeekPosition", None),
		"FreeBufferSpace": (1, 2, (3, 0), (), "FreeBufferSpace", None),
		"NonBlockingIO": (2, 2, (3, 0), (), "NonBlockingIO", None),
		"State": (3, 2, (3, 0), (), "State", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechBaseStream(DispatchBaseClass):
	'ISpeechBaseStream Interface'
	CLSID = IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')
	coclass_clsid = None

	def Read(self, Buffer=pythoncom.Missing, NumberOfBytes=defaultNamedNotOptArg):
		'Read'
		return self._ApplyTypes_(2, 1, (3, 0), ((16396, 2), (3, 1)), u'Read', None,Buffer
			, NumberOfBytes)

	def Seek(self, Position=defaultNamedNotOptArg, Origin=0):
		'Seek'
		return self._ApplyTypes_(4, 1, (12, 0), ((12, 1), (3, 49)), u'Seek', None,Position
			, Origin)

	def Write(self, Buffer=defaultNamedNotOptArg):
		'Write'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((12, 1),),Buffer
			)

	_prop_map_get_ = {
		# Method 'Format' returns object of type 'ISpeechAudioFormat'
		"Format": (1, 2, (9, 0), (), "Format", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
	}
	_prop_map_put_ = {
		"Format": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechCustomStream(DispatchBaseClass):
	'ISpeechCustomStream Interface'
	CLSID = IID('{1A9E9F4F-104F-4DB8-A115-EFD7FD0C97AE}')
	coclass_clsid = IID('{8DBEF13F-1948-4AA8-8CF0-048EEBED95D8}')

	def Read(self, Buffer=pythoncom.Missing, NumberOfBytes=defaultNamedNotOptArg):
		'Read'
		return self._ApplyTypes_(2, 1, (3, 0), ((16396, 2), (3, 1)), u'Read', None,Buffer
			, NumberOfBytes)

	def Seek(self, Position=defaultNamedNotOptArg, Origin=0):
		'Seek'
		return self._ApplyTypes_(4, 1, (12, 0), ((12, 1), (3, 49)), u'Seek', None,Position
			, Origin)

	def Write(self, Buffer=defaultNamedNotOptArg):
		'Write'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((12, 1),),Buffer
			)

	_prop_map_get_ = {
		"BaseStream": (100, 2, (13, 0), (), "BaseStream", None),
		# Method 'Format' returns object of type 'ISpeechAudioFormat'
		"Format": (1, 2, (9, 0), (), "Format", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
	}
	_prop_map_put_ = {
		"BaseStream": ((100, LCID, 8, 0),()),
		"Format": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechDataKey(DispatchBaseClass):
	'ISpeechDataKey Interface'
	CLSID = IID('{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}')
	coclass_clsid = None

	# Result is of type ISpeechDataKey
	def CreateKey(self, SubKeyName=defaultNamedNotOptArg):
		'CreateKey'
		ret = self._oleobj_.InvokeTypes(8, LCID, 1, (9, 0), ((8, 1),),SubKeyName
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreateKey', '{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}')
		return ret

	def DeleteKey(self, SubKeyName=defaultNamedNotOptArg):
		'DeleteKey'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((8, 1),),SubKeyName
			)

	def DeleteValue(self, ValueName=defaultNamedNotOptArg):
		'DeleteValue'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((8, 1),),ValueName
			)

	def EnumKeys(self, Index=defaultNamedNotOptArg):
		'EnumKeys'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(11, LCID, 1, (8, 0), ((3, 1),),Index
			)

	def EnumValues(self, Index=defaultNamedNotOptArg):
		'EnumValues'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(12, LCID, 1, (8, 0), ((3, 1),),Index
			)

	def GetBinaryValue(self, ValueName=defaultNamedNotOptArg):
		'GetBinaryValue'
		return self._ApplyTypes_(2, 1, (12, 0), ((8, 1),), u'GetBinaryValue', None,ValueName
			)

	def GetLongValue(self, ValueName=defaultNamedNotOptArg):
		'GetlongValue'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (3, 0), ((8, 1),),ValueName
			)

	def GetStringValue(self, ValueName=defaultNamedNotOptArg):
		'GetStringValue'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(4, LCID, 1, (8, 0), ((8, 1),),ValueName
			)

	# Result is of type ISpeechDataKey
	def OpenKey(self, SubKeyName=defaultNamedNotOptArg):
		'OpenKey'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((8, 1),),SubKeyName
			)
		if ret is not None:
			ret = Dispatch(ret, u'OpenKey', '{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}')
		return ret

	def SetBinaryValue(self, ValueName=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'SetBinaryValue'
		return self._oleobj_.InvokeTypes(1, LCID, 1, (24, 0), ((8, 1), (12, 1)),ValueName
			, Value)

	def SetLongValue(self, ValueName=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'SetLongValue'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((8, 1), (3, 1)),ValueName
			, Value)

	def SetStringValue(self, ValueName=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'SetStringValue'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1), (8, 1)),ValueName
			, Value)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechFileStream(DispatchBaseClass):
	'ISpeechFileStream Interface'
	CLSID = IID('{AF67F125-AB39-4E93-B4A2-CC2E66E182A7}')
	coclass_clsid = IID('{947812B3-2AE1-4644-BA86-9E90DED7EC91}')

	def Close(self):
		'Close'
		return self._oleobj_.InvokeTypes(101, LCID, 1, (24, 0), (),)

	def Open(self, FileName=defaultNamedNotOptArg, FileMode=0, DoEvents=False):
		'Open'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), ((8, 1), (3, 49), (11, 49)),FileName
			, FileMode, DoEvents)

	def Read(self, Buffer=pythoncom.Missing, NumberOfBytes=defaultNamedNotOptArg):
		'Read'
		return self._ApplyTypes_(2, 1, (3, 0), ((16396, 2), (3, 1)), u'Read', None,Buffer
			, NumberOfBytes)

	def Seek(self, Position=defaultNamedNotOptArg, Origin=0):
		'Seek'
		return self._ApplyTypes_(4, 1, (12, 0), ((12, 1), (3, 49)), u'Seek', None,Position
			, Origin)

	def Write(self, Buffer=defaultNamedNotOptArg):
		'Write'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((12, 1),),Buffer
			)

	_prop_map_get_ = {
		# Method 'Format' returns object of type 'ISpeechAudioFormat'
		"Format": (1, 2, (9, 0), (), "Format", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
	}
	_prop_map_put_ = {
		"Format": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechGrammarRule(DispatchBaseClass):
	'ISpeechGrammarRule Interface'
	CLSID = IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
	coclass_clsid = None

	def AddResource(self, ResourceName=defaultNamedNotOptArg, ResourceValue=defaultNamedNotOptArg):
		'AddResource'
		return self._oleobj_.InvokeTypes(6, LCID, 1, (24, 0), ((8, 1), (8, 1)),ResourceName
			, ResourceValue)

	# Result is of type ISpeechGrammarRuleState
	def AddState(self):
		'AddState'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'AddState', '{D4286F2C-EE67-45AE-B928-28D695362EDA}')
		return ret

	def Clear(self):
		'Clear'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"Attributes": (1, 2, (3, 0), (), "Attributes", None),
		"Id": (4, 2, (3, 0), (), "Id", None),
		# Method 'InitialState' returns object of type 'ISpeechGrammarRuleState'
		"InitialState": (2, 2, (9, 0), (), "InitialState", '{D4286F2C-EE67-45AE-B928-28D695362EDA}'),
		"Name": (3, 2, (8, 0), (), "Name", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechGrammarRuleState(DispatchBaseClass):
	'ISpeechGrammarRuleState Interface'
	CLSID = IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')
	coclass_clsid = None

	def AddRuleTransition(self, DestinationState=defaultNamedNotOptArg, Rule=defaultNamedNotOptArg, PropertyName=u'', PropertyId=0
			, PropertyValue=u'', Weight=1.0):
		'AddRuleTransition'
		return self._ApplyTypes_(4, 1, (24, 32), ((9, 1), (9, 1), (8, 49), (3, 49), (16396, 49), (4, 49)), u'AddRuleTransition', None,DestinationState
			, Rule, PropertyName, PropertyId, PropertyValue, Weight
			)

	def AddSpecialTransition(self, DestinationState=defaultNamedNotOptArg, Type=defaultNamedNotOptArg, PropertyName=u'', PropertyId=0
			, PropertyValue=u'', Weight=1.0):
		'AddSpecialTransition'
		return self._ApplyTypes_(5, 1, (24, 32), ((9, 1), (3, 1), (8, 49), (3, 49), (16396, 49), (4, 49)), u'AddSpecialTransition', None,DestinationState
			, Type, PropertyName, PropertyId, PropertyValue, Weight
			)

	def AddWordTransition(self, DestState=defaultNamedNotOptArg, Words=defaultNamedNotOptArg, Separators=u' ', Type=1
			, PropertyName=u'', PropertyId=0, PropertyValue=u'', Weight=1.0):
		'AddWordTransition'
		return self._ApplyTypes_(3, 1, (24, 32), ((9, 1), (8, 1), (8, 49), (3, 49), (8, 49), (3, 49), (16396, 49), (4, 49)), u'AddWordTransition', None,DestState
			, Words, Separators, Type, PropertyName, PropertyId
			, PropertyValue, Weight)

	_prop_map_get_ = {
		# Method 'Rule' returns object of type 'ISpeechGrammarRule'
		"Rule": (1, 2, (9, 0), (), "Rule", '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}'),
		# Method 'Transitions' returns object of type 'ISpeechGrammarRuleStateTransitions'
		"Transitions": (2, 2, (9, 0), (), "Transitions", '{EABCE657-75BC-44A2-AA7F-C56476742963}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechGrammarRuleStateTransition(DispatchBaseClass):
	'ISpeechGrammarRuleStateTransition Interface'
	CLSID = IID('{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'NextState' returns object of type 'ISpeechGrammarRuleState'
		"NextState": (8, 2, (9, 0), (), "NextState", '{D4286F2C-EE67-45AE-B928-28D695362EDA}'),
		"PropertyId": (6, 2, (3, 0), (), "PropertyId", None),
		"PropertyName": (5, 2, (8, 0), (), "PropertyName", None),
		"PropertyValue": (7, 2, (12, 0), (), "PropertyValue", None),
		# Method 'Rule' returns object of type 'ISpeechGrammarRule'
		"Rule": (3, 2, (9, 0), (), "Rule", '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}'),
		"Text": (2, 2, (8, 0), (), "Text", None),
		"Type": (1, 2, (3, 0), (), "Type", None),
		"Weight": (4, 2, (12, 0), (), "Weight", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechGrammarRuleStateTransitions(DispatchBaseClass):
	'ISpeechGrammarRuleStateTransitions Interface'
	CLSID = IID('{EABCE657-75BC-44A2-AA7F-C56476742963}')
	coclass_clsid = None

	# Result is of type ISpeechGrammarRuleStateTransition
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechGrammarRules(DispatchBaseClass):
	'ISpeechGrammarRules Interface'
	CLSID = IID('{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}')
	coclass_clsid = None

	# Result is of type ISpeechGrammarRule
	def Add(self, RuleName=defaultNamedNotOptArg, Attributes=defaultNamedNotOptArg, RuleId=0):
		'Add'
		ret = self._oleobj_.InvokeTypes(3, LCID, 1, (9, 0), ((8, 1), (3, 1), (3, 49)),RuleName
			, Attributes, RuleId)
		if ret is not None:
			ret = Dispatch(ret, u'Add', '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
		return ret

	def Commit(self):
		'Commit'
		return self._oleobj_.InvokeTypes(4, LCID, 1, (24, 0), (),)

	def CommitAndSave(self, ErrorText=pythoncom.Missing):
		'CommitAndSave'
		return self._ApplyTypes_(5, 1, (12, 0), ((16392, 2),), u'CommitAndSave', None,ErrorText
			)

	# Result is of type ISpeechGrammarRule
	def FindRule(self, RuleNameOrId=defaultNamedNotOptArg):
		'FindRule'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((12, 1),),RuleNameOrId
			)
		if ret is not None:
			ret = Dispatch(ret, u'FindRule', '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
		return ret

	# Result is of type ISpeechGrammarRule
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"Dynamic": (2, 2, (11, 0), (), "Dynamic", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechLexicon(DispatchBaseClass):
	'ISpeechLexicon Interface'
	CLSID = IID('{3DA7627A-C7AE-4B23-8708-638C50362C25}')
	coclass_clsid = IID('{C9E37C15-DF92-4727-85D6-72E5EEB6995A}')

	def AddPronunciation(self, bstrWord=defaultNamedNotOptArg, LangId=defaultNamedNotOptArg, PartOfSpeech=0, bstrPronunciation=u''):
		'AddPronunciation'
		return self._ApplyTypes_(3, 1, (24, 32), ((8, 1), (3, 1), (3, 49), (8, 49)), u'AddPronunciation', None,bstrWord
			, LangId, PartOfSpeech, bstrPronunciation)

	def AddPronunciationByPhoneIds(self, bstrWord=defaultNamedNotOptArg, LangId=defaultNamedNotOptArg, PartOfSpeech=0, PhoneIds=u''):
		'AddPronunciationByPhoneIds'
		return self._ApplyTypes_(4, 1, (24, 32), ((8, 1), (3, 1), (3, 49), (16396, 49)), u'AddPronunciationByPhoneIds', None,bstrWord
			, LangId, PartOfSpeech, PhoneIds)

	# Result is of type ISpeechLexiconWords
	def GetGenerationChange(self, GenerationId=defaultNamedNotOptArg):
		'GetGenerationChange'
		return self._ApplyTypes_(8, 1, (9, 0), ((16387, 3),), u'GetGenerationChange', '{8D199862-415E-47D5-AC4F-FAA608B424E6}',GenerationId
			)

	# Result is of type ISpeechLexiconPronunciations
	def GetPronunciations(self, bstrWord=defaultNamedNotOptArg, LangId=0, TypeFlags=3):
		'GetPronunciations'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (9, 0), ((8, 1), (3, 49), (3, 49)),bstrWord
			, LangId, TypeFlags)
		if ret is not None:
			ret = Dispatch(ret, u'GetPronunciations', '{72829128-5682-4704-A0D4-3E2BB6F2EAD3}')
		return ret

	# Result is of type ISpeechLexiconWords
	def GetWords(self, Flags=3, GenerationId=0):
		'GetWords'
		return self._ApplyTypes_(2, 1, (9, 0), ((3, 49), (16387, 50)), u'GetWords', '{8D199862-415E-47D5-AC4F-FAA608B424E6}',Flags
			, GenerationId)

	def RemovePronunciation(self, bstrWord=defaultNamedNotOptArg, LangId=defaultNamedNotOptArg, PartOfSpeech=0, bstrPronunciation=u''):
		'RemovePronunciation'
		return self._ApplyTypes_(5, 1, (24, 32), ((8, 1), (3, 1), (3, 49), (8, 49)), u'RemovePronunciation', None,bstrWord
			, LangId, PartOfSpeech, bstrPronunciation)

	def RemovePronunciationByPhoneIds(self, bstrWord=defaultNamedNotOptArg, LangId=defaultNamedNotOptArg, PartOfSpeech=0, PhoneIds=u''):
		'RemovePronunciationByPhoneIds'
		return self._ApplyTypes_(6, 1, (24, 32), ((8, 1), (3, 1), (3, 49), (16396, 49)), u'RemovePronunciationByPhoneIds', None,bstrWord
			, LangId, PartOfSpeech, PhoneIds)

	_prop_map_get_ = {
		"GenerationId": (1, 2, (3, 0), (), "GenerationId", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechLexiconPronunciation(DispatchBaseClass):
	'ISpeechLexiconPronunciation Interface'
	CLSID = IID('{95252C5D-9E43-4F4A-9899-48EE73352F9F}')
	coclass_clsid = None

	_prop_map_get_ = {
		"LangId": (2, 2, (3, 0), (), "LangId", None),
		"PartOfSpeech": (3, 2, (3, 0), (), "PartOfSpeech", None),
		"PhoneIds": (4, 2, (12, 0), (), "PhoneIds", None),
		"Symbolic": (5, 2, (8, 0), (), "Symbolic", None),
		"Type": (1, 2, (3, 0), (), "Type", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechLexiconPronunciations(DispatchBaseClass):
	'ISpeechLexiconPronunciations Interface'
	CLSID = IID('{72829128-5682-4704-A0D4-3E2BB6F2EAD3}')
	coclass_clsid = None

	# Result is of type ISpeechLexiconPronunciation
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{95252C5D-9E43-4F4A-9899-48EE73352F9F}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{95252C5D-9E43-4F4A-9899-48EE73352F9F}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{95252C5D-9E43-4F4A-9899-48EE73352F9F}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechLexiconWord(DispatchBaseClass):
	'ISpeechLexiconWord Interface'
	CLSID = IID('{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}')
	coclass_clsid = None

	_prop_map_get_ = {
		"LangId": (1, 2, (3, 0), (), "LangId", None),
		# Method 'Pronunciations' returns object of type 'ISpeechLexiconPronunciations'
		"Pronunciations": (4, 2, (9, 0), (), "Pronunciations", '{72829128-5682-4704-A0D4-3E2BB6F2EAD3}'),
		"Type": (2, 2, (3, 0), (), "Type", None),
		"Word": (3, 2, (8, 0), (), "Word", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechLexiconWords(DispatchBaseClass):
	'ISpeechLexiconWords Interface'
	CLSID = IID('{8D199862-415E-47D5-AC4F-FAA608B424E6}')
	coclass_clsid = None

	# Result is of type ISpeechLexiconWord
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechMMSysAudio(DispatchBaseClass):
	'ISpeechMMSysAudio Interface'
	CLSID = IID('{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}')
	coclass_clsid = IID('{A8C680EB-3D32-11D2-9EE7-00C04F797396}')

	def Read(self, Buffer=pythoncom.Missing, NumberOfBytes=defaultNamedNotOptArg):
		'Read'
		return self._ApplyTypes_(2, 1, (3, 0), ((16396, 2), (3, 1)), u'Read', None,Buffer
			, NumberOfBytes)

	def Seek(self, Position=defaultNamedNotOptArg, Origin=0):
		'Seek'
		return self._ApplyTypes_(4, 1, (12, 0), ((12, 1), (3, 49)), u'Seek', None,Position
			, Origin)

	def SetState(self, State=defaultNamedNotOptArg):
		'SetState'
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), ((3, 1),),State
			)

	def Write(self, Buffer=defaultNamedNotOptArg):
		'Write'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((12, 1),),Buffer
			)

	_prop_map_get_ = {
		# Method 'BufferInfo' returns object of type 'ISpeechAudioBufferInfo'
		"BufferInfo": (201, 2, (9, 0), (), "BufferInfo", '{11B103D8-1142-4EDF-A093-82FB3915F8CC}'),
		"BufferNotifySize": (204, 2, (3, 0), (), "BufferNotifySize", None),
		# Method 'DefaultFormat' returns object of type 'ISpeechAudioFormat'
		"DefaultFormat": (202, 2, (9, 0), (), "DefaultFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		"DeviceId": (300, 2, (3, 0), (), "DeviceId", None),
		"EventHandle": (205, 2, (3, 0), (), "EventHandle", None),
		# Method 'Format' returns object of type 'ISpeechAudioFormat'
		"Format": (1, 2, (9, 0), (), "Format", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		"LineId": (301, 2, (3, 0), (), "LineId", None),
		"MMHandle": (302, 2, (3, 0), (), "MMHandle", None),
		# Method 'Status' returns object of type 'ISpeechAudioStatus'
		"Status": (200, 2, (9, 0), (), "Status", '{C62D9C91-7458-47F6-862D-1EF86FB0B278}'),
		"Volume": (203, 2, (3, 0), (), "Volume", None),
	}
	_prop_map_put_ = {
		"BufferNotifySize": ((204, LCID, 4, 0),()),
		"DeviceId": ((300, LCID, 4, 0),()),
		"Format": ((1, LCID, 8, 0),()),
		"LineId": ((301, LCID, 4, 0),()),
		"Volume": ((203, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechMemoryStream(DispatchBaseClass):
	'ISpeechMemoryStream Interface'
	CLSID = IID('{EEB14B68-808B-4ABE-A5EA-B51DA7588008}')
	coclass_clsid = IID('{5FB7EF7D-DFF4-468A-B6B7-2FCBD188F994}')

	def GetData(self):
		'GetData'
		return self._ApplyTypes_(101, 1, (12, 0), (), u'GetData', None,)

	def Read(self, Buffer=pythoncom.Missing, NumberOfBytes=defaultNamedNotOptArg):
		'Read'
		return self._ApplyTypes_(2, 1, (3, 0), ((16396, 2), (3, 1)), u'Read', None,Buffer
			, NumberOfBytes)

	def Seek(self, Position=defaultNamedNotOptArg, Origin=0):
		'Seek'
		return self._ApplyTypes_(4, 1, (12, 0), ((12, 1), (3, 49)), u'Seek', None,Position
			, Origin)

	def SetData(self, Data=defaultNamedNotOptArg):
		'SetData'
		return self._oleobj_.InvokeTypes(100, LCID, 1, (24, 0), ((12, 1),),Data
			)

	def Write(self, Buffer=defaultNamedNotOptArg):
		'Write'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (3, 0), ((12, 1),),Buffer
			)

	_prop_map_get_ = {
		# Method 'Format' returns object of type 'ISpeechAudioFormat'
		"Format": (1, 2, (9, 0), (), "Format", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
	}
	_prop_map_put_ = {
		"Format": ((1, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechObjectToken(DispatchBaseClass):
	'ISpeechObjectToken Interface'
	CLSID = IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')
	coclass_clsid = IID('{EF411752-3736-4CB4-9C8C-8EF4CCB58EFE}')

	def CreateInstance(self, pUnkOuter=None, ClsContext=23):
		'CreateInstance'
		ret = self._oleobj_.InvokeTypes(7, LCID, 1, (13, 0), ((13, 49), (3, 49)),pUnkOuter
			, ClsContext)
		if ret is not None:
			# See if this IUnknown is really an IDispatch
			try:
				ret = ret.QueryInterface(pythoncom.IID_IDispatch)
			except pythoncom.error:
				return ret
			ret = Dispatch(ret, u'CreateInstance', None)
		return ret

	def DisplayUI(self, hWnd=defaultNamedNotOptArg, Title=defaultNamedNotOptArg, TypeOfUI=defaultNamedNotOptArg, ExtraData=u''
			, Object=None):
		'DisplayUI'
		return self._ApplyTypes_(12, 1, (24, 32), ((3, 1), (8, 1), (8, 1), (16396, 49), (13, 49)), u'DisplayUI', None,hWnd
			, Title, TypeOfUI, ExtraData, Object)

	def GetAttribute(self, AttributeName=defaultNamedNotOptArg):
		'GetAttribute'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(6, LCID, 1, (8, 0), ((8, 1),),AttributeName
			)

	def GetDescription(self, Locale=0):
		'GetDescription'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(4, LCID, 1, (8, 0), ((3, 49),),Locale
			)

	def GetStorageFileName(self, ObjectStorageCLSID=defaultNamedNotOptArg, KeyName=defaultNamedNotOptArg, FileName=defaultNamedNotOptArg, Folder=defaultNamedNotOptArg):
		'GetStorageFileName'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(9, LCID, 1, (8, 0), ((8, 1), (8, 1), (8, 1), (3, 1)),ObjectStorageCLSID
			, KeyName, FileName, Folder)

	def IsUISupported(self, TypeOfUI=defaultNamedNotOptArg, ExtraData=u'', Object=None):
		'IsUISupported'
		return self._ApplyTypes_(11, 1, (11, 32), ((8, 1), (16396, 49), (13, 49)), u'IsUISupported', None,TypeOfUI
			, ExtraData, Object)

	def MatchesAttributes(self, Attributes=defaultNamedNotOptArg):
		'MatchesAttributes'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (11, 0), ((8, 1),),Attributes
			)

	def Remove(self, ObjectStorageCLSID=defaultNamedNotOptArg):
		'Remove'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((8, 1),),ObjectStorageCLSID
			)

	def RemoveStorageFileName(self, ObjectStorageCLSID=defaultNamedNotOptArg, KeyName=defaultNamedNotOptArg, DeleteFile=defaultNamedNotOptArg):
		'RemoveStorageFileName'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((8, 1), (8, 1), (11, 1)),ObjectStorageCLSID
			, KeyName, DeleteFile)

	def SetId(self, Id=defaultNamedNotOptArg, CategoryID=u'', CreateIfNotExist=False):
		'SetId'
		return self._ApplyTypes_(5, 1, (24, 32), ((8, 1), (8, 49), (11, 49)), u'SetId', None,Id
			, CategoryID, CreateIfNotExist)

	_prop_map_get_ = {
		# Method 'Category' returns object of type 'ISpeechObjectTokenCategory'
		"Category": (3, 2, (9, 0), (), "Category", '{CA7EAC50-2D01-4145-86D4-5AE7D70F4469}'),
		# Method 'DataKey' returns object of type 'ISpeechDataKey'
		"DataKey": (2, 2, (9, 0), (), "DataKey", '{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}'),
		"Id": (1, 2, (8, 0), (), "Id", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechObjectTokenCategory(DispatchBaseClass):
	'ISpeechObjectTokenCategory Interface'
	CLSID = IID('{CA7EAC50-2D01-4145-86D4-5AE7D70F4469}')
	coclass_clsid = IID('{A910187F-0C7A-45AC-92CC-59EDAFB77B53}')

	# Result is of type ISpeechObjectTokens
	def EnumerateTokens(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'EnumerateTokens'
		return self._ApplyTypes_(5, 1, (9, 32), ((8, 49), (8, 49)), u'EnumerateTokens', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	# Result is of type ISpeechDataKey
	def GetDataKey(self, Location=0):
		'GetDataKey'
		ret = self._oleobj_.InvokeTypes(4, LCID, 1, (9, 0), ((3, 49),),Location
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetDataKey', '{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}')
		return ret

	def SetId(self, Id=defaultNamedNotOptArg, CreateIfNotExist=False):
		'SetId'
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1), (11, 49)),Id
			, CreateIfNotExist)

	_prop_map_get_ = {
		"Default": (2, 2, (8, 0), (), "Default", None),
		"Id": (1, 2, (8, 0), (), "Id", None),
	}
	_prop_map_put_ = {
		"Default": ((2, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechObjectTokens(DispatchBaseClass):
	'ISpeechObjectTokens Interface'
	CLSID = IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')
	coclass_clsid = None

	# Result is of type ISpeechObjectToken
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{C74A3ADC-B727-4500-A84A-B526721C8B8C}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C74A3ADC-B727-4500-A84A-B526721C8B8C}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{C74A3ADC-B727-4500-A84A-B526721C8B8C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechPhoneConverter(DispatchBaseClass):
	'ISpeechPhoneConverter Interface'
	CLSID = IID('{C3E4F353-433F-43D6-89A1-6A62A7054C3D}')
	coclass_clsid = IID('{9185F743-1143-4C28-86B5-BFF14F20E5C8}')

	def IdToPhone(self, IdArray=defaultNamedNotOptArg):
		'IdToPhone'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(3, LCID, 1, (8, 0), ((12, 1),),IdArray
			)

	def PhoneToId(self, Phonemes=defaultNamedNotOptArg):
		'PhoneToId'
		return self._ApplyTypes_(2, 1, (12, 0), ((8, 1),), u'PhoneToId', None,Phonemes
			)

	_prop_map_get_ = {
		"LanguageId": (1, 2, (3, 0), (), "LanguageId", None),
	}
	_prop_map_put_ = {
		"LanguageId": ((1, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechPhraseAlternate(DispatchBaseClass):
	'ISpeechPhraseAlternate Interface'
	CLSID = IID('{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}')
	coclass_clsid = None

	def Commit(self):
		'Commit'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), (),)

	_prop_map_get_ = {
		"NumberOfElementsInResult": (3, 2, (3, 0), (), "NumberOfElementsInResult", None),
		# Method 'PhraseInfo' returns object of type 'ISpeechPhraseInfo'
		"PhraseInfo": (4, 2, (9, 0), (), "PhraseInfo", '{961559CF-4E67-4662-8BF0-D93F1FCD61B3}'),
		# Method 'RecoResult' returns object of type 'ISpeechRecoResult'
		"RecoResult": (1, 2, (9, 0), (), "RecoResult", '{ED2879CF-CED9-4EE6-A534-DE0191D5468D}'),
		"StartElementInResult": (2, 2, (3, 0), (), "StartElementInResult", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechPhraseAlternates(DispatchBaseClass):
	'ISpeechPhraseAlternates Interface'
	CLSID = IID('{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseAlternate
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechPhraseElement(DispatchBaseClass):
	'ISpeechPhraseElement Interface'
	CLSID = IID('{E6176F96-E373-4801-B223-3B62C068C0B4}')
	coclass_clsid = None

	_prop_map_get_ = {
		"ActualConfidence": (12, 2, (3, 0), (), "ActualConfidence", None),
		"AudioSizeBytes": (4, 2, (3, 0), (), "AudioSizeBytes", None),
		"AudioSizeTime": (2, 2, (3, 0), (), "AudioSizeTime", None),
		"AudioStreamOffset": (3, 2, (3, 0), (), "AudioStreamOffset", None),
		"AudioTimeOffset": (1, 2, (3, 0), (), "AudioTimeOffset", None),
		"DisplayAttributes": (10, 2, (3, 0), (), "DisplayAttributes", None),
		"DisplayText": (7, 2, (8, 0), (), "DisplayText", None),
		"EngineConfidence": (13, 2, (4, 0), (), "EngineConfidence", None),
		"LexicalForm": (8, 2, (8, 0), (), "LexicalForm", None),
		"Pronunciation": (9, 2, (12, 0), (), "Pronunciation", None),
		"RequiredConfidence": (11, 2, (3, 0), (), "RequiredConfidence", None),
		"RetainedSizeBytes": (6, 2, (3, 0), (), "RetainedSizeBytes", None),
		"RetainedStreamOffset": (5, 2, (3, 0), (), "RetainedStreamOffset", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechPhraseElements(DispatchBaseClass):
	'ISpeechPhraseElements Interface'
	CLSID = IID('{0626B328-3478-467D-A0B3-D0853B93DDA3}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseElement
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{E6176F96-E373-4801-B223-3B62C068C0B4}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E6176F96-E373-4801-B223-3B62C068C0B4}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E6176F96-E373-4801-B223-3B62C068C0B4}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechPhraseInfo(DispatchBaseClass):
	'ISpeechPhraseInfo Interface'
	CLSID = IID('{961559CF-4E67-4662-8BF0-D93F1FCD61B3}')
	coclass_clsid = None

	def GetDisplayAttributes(self, StartElement=0, Elements=-1, UseReplacements=True):
		'DisplayAttributes'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((3, 49), (3, 49), (11, 49)),StartElement
			, Elements, UseReplacements)

	def GetText(self, StartElement=0, Elements=-1, UseReplacements=True):
		'GetText'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(15, LCID, 1, (8, 0), ((3, 49), (3, 49), (11, 49)),StartElement
			, Elements, UseReplacements)

	def SaveToMemory(self):
		'SaveToMemory'
		return self._ApplyTypes_(14, 1, (12, 0), (), u'SaveToMemory', None,)

	_prop_map_get_ = {
		"AudioSizeBytes": (5, 2, (3, 0), (), "AudioSizeBytes", None),
		"AudioSizeTime": (7, 2, (3, 0), (), "AudioSizeTime", None),
		"AudioStreamPosition": (4, 2, (12, 0), (), "AudioStreamPosition", None),
		# Method 'Elements' returns object of type 'ISpeechPhraseElements'
		"Elements": (10, 2, (9, 0), (), "Elements", '{0626B328-3478-467D-A0B3-D0853B93DDA3}'),
		"EngineId": (12, 2, (8, 0), (), "EngineId", None),
		"EnginePrivateData": (13, 2, (12, 0), (), "EnginePrivateData", None),
		"GrammarId": (2, 2, (12, 0), (), "GrammarId", None),
		"LanguageId": (1, 2, (3, 0), (), "LanguageId", None),
		# Method 'Properties' returns object of type 'ISpeechPhraseProperties'
		"Properties": (9, 2, (9, 0), (), "Properties", '{08166B47-102E-4B23-A599-BDB98DBFD1F4}'),
		# Method 'Replacements' returns object of type 'ISpeechPhraseReplacements'
		"Replacements": (11, 2, (9, 0), (), "Replacements", '{38BC662F-2257-4525-959E-2069D2596C05}'),
		"RetainedSizeBytes": (6, 2, (3, 0), (), "RetainedSizeBytes", None),
		# Method 'Rule' returns object of type 'ISpeechPhraseRule'
		"Rule": (8, 2, (9, 0), (), "Rule", '{A7BFE112-A4A0-48D9-B602-C313843F6964}'),
		"StartTime": (3, 2, (12, 0), (), "StartTime", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechPhraseInfoBuilder(DispatchBaseClass):
	'ISpeechPhraseInfoBuilder Interface'
	CLSID = IID('{3B151836-DF3A-4E0A-846C-D2ADC9334333}')
	coclass_clsid = IID('{C23FC28D-C55F-4720-8B32-91F73C2BD5D1}')

	# Result is of type ISpeechPhraseInfo
	def RestorePhraseFromMemory(self, PhraseInMemory=defaultNamedNotOptArg):
		'RestorePhraseFromMemory'
		ret = self._oleobj_.InvokeTypes(1, LCID, 1, (9, 0), ((16396, 1),),PhraseInMemory
			)
		if ret is not None:
			ret = Dispatch(ret, u'RestorePhraseFromMemory', '{961559CF-4E67-4662-8BF0-D93F1FCD61B3}')
		return ret

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechPhraseProperties(DispatchBaseClass):
	'ISpeechPhraseProperties Interface'
	CLSID = IID('{08166B47-102E-4B23-A599-BDB98DBFD1F4}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseProperty
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{CE563D48-961E-4732-A2E1-378A42B430BE}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CE563D48-961E-4732-A2E1-378A42B430BE}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CE563D48-961E-4732-A2E1-378A42B430BE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechPhraseProperty(DispatchBaseClass):
	'ISpeechPhraseProperty Interface'
	CLSID = IID('{CE563D48-961E-4732-A2E1-378A42B430BE}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Children' returns object of type 'ISpeechPhraseProperties'
		"Children": (9, 2, (9, 0), (), "Children", '{08166B47-102E-4B23-A599-BDB98DBFD1F4}'),
		"Confidence": (7, 2, (3, 0), (), "Confidence", None),
		"EngineConfidence": (6, 2, (4, 0), (), "EngineConfidence", None),
		"FirstElement": (4, 2, (3, 0), (), "FirstElement", None),
		"Id": (2, 2, (3, 0), (), "Id", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"NumberOfElements": (5, 2, (3, 0), (), "NumberOfElements", None),
		# Method 'Parent' returns object of type 'ISpeechPhraseProperty'
		"Parent": (8, 2, (9, 0), (), "Parent", '{CE563D48-961E-4732-A2E1-378A42B430BE}'),
		"Value": (3, 2, (12, 0), (), "Value", None),
	}
	_prop_map_put_ = {
	}
	# Default property for this class is 'Value'
	def __call__(self):
		return self._ApplyTypes_(*(3, 2, (12, 0), (), "Value", None))
	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechPhraseReplacement(DispatchBaseClass):
	'ISpeechPhraseReplacement Interface'
	CLSID = IID('{2890A410-53A7-4FB5-94EC-06D4998E3D02}')
	coclass_clsid = None

	_prop_map_get_ = {
		"DisplayAttributes": (1, 2, (3, 0), (), "DisplayAttributes", None),
		"FirstElement": (3, 2, (3, 0), (), "FirstElement", None),
		"NumberOfElements": (4, 2, (3, 0), (), "NumberOfElements", None),
		"Text": (2, 2, (8, 0), (), "Text", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechPhraseReplacements(DispatchBaseClass):
	'ISpeechPhraseReplacements Interface'
	CLSID = IID('{38BC662F-2257-4525-959E-2069D2596C05}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseReplacement
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{2890A410-53A7-4FB5-94EC-06D4998E3D02}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{2890A410-53A7-4FB5-94EC-06D4998E3D02}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{2890A410-53A7-4FB5-94EC-06D4998E3D02}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechPhraseRule(DispatchBaseClass):
	'ISpeechPhraseRule Interface'
	CLSID = IID('{A7BFE112-A4A0-48D9-B602-C313843F6964}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'Children' returns object of type 'ISpeechPhraseRules'
		"Children": (6, 2, (9, 0), (), "Children", '{9047D593-01DD-4B72-81A3-E4A0CA69F407}'),
		"Confidence": (7, 2, (3, 0), (), "Confidence", None),
		"EngineConfidence": (8, 2, (4, 0), (), "EngineConfidence", None),
		"FirstElement": (3, 2, (3, 0), (), "FirstElement", None),
		"Id": (2, 2, (3, 0), (), "Id", None),
		"Name": (1, 2, (8, 0), (), "Name", None),
		"NumberOfElements": (4, 2, (3, 0), (), "NumberOfElements", None),
		# Method 'Parent' returns object of type 'ISpeechPhraseRule'
		"Parent": (5, 2, (9, 0), (), "Parent", '{A7BFE112-A4A0-48D9-B602-C313843F6964}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechPhraseRules(DispatchBaseClass):
	'ISpeechPhraseRules Interface'
	CLSID = IID('{9047D593-01DD-4B72-81A3-E4A0CA69F407}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseRule
	def Item(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, u'Item', '{A7BFE112-A4A0-48D9-B602-C313843F6964}')
		return ret

	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
	}
	_prop_map_put_ = {
	}
	# Default method for this class is 'Item'
	def __call__(self, Index=defaultNamedNotOptArg):
		'Item'
		ret = self._oleobj_.InvokeTypes(0, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A7BFE112-A4A0-48D9-B602-C313843F6964}')
		return ret

	def __unicode__(self, *args):
		try:
			return unicode(self.__call__(*args))
		except pythoncom.com_error:
			return repr(self)
	def __str__(self, *args):
		return str(self.__unicode__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{A7BFE112-A4A0-48D9-B602-C313843F6964}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ISpeechRecoContext(DispatchBaseClass):
	'ISpeechRecoContext Interface'
	CLSID = IID('{580AA49D-7E1E-4809-B8E2-57DA806104B8}')
	coclass_clsid = IID('{73AD6842-ACE0-45E8-A4DD-8795881A2C2A}')

	def Bookmark(self, Options=defaultNamedNotOptArg, StreamPos=defaultNamedNotOptArg, BookmarkId=defaultNamedNotOptArg):
		'Bookmark'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 1)),Options
			, StreamPos, BookmarkId)

	# Result is of type ISpeechRecoGrammar
	def CreateGrammar(self, GrammarId=0):
		'CreateGrammar'
		ret = self._oleobj_.InvokeTypes(14, LCID, 1, (9, 0), ((12, 49),),GrammarId
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreateGrammar', '{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}')
		return ret

	# Result is of type ISpeechRecoResult
	def CreateResultFromMemory(self, ResultBlock=defaultNamedNotOptArg):
		'CreateResultFromMemory'
		ret = self._oleobj_.InvokeTypes(15, LCID, 1, (9, 0), ((16396, 1),),ResultBlock
			)
		if ret is not None:
			ret = Dispatch(ret, u'CreateResultFromMemory', '{ED2879CF-CED9-4EE6-A534-DE0191D5468D}')
		return ret

	def Pause(self):
		'Pause'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), (),)

	def Resume(self):
		'Resume'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), (),)

	def SetAdaptationData(self, AdaptationString=defaultNamedNotOptArg):
		'SetAdaptationData'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1),),AdaptationString
			)

	_prop_map_get_ = {
		"AllowVoiceFormatMatchingOnNextSet": (5, 2, (11, 0), (), "AllowVoiceFormatMatchingOnNextSet", None),
		"AudioInputInterferenceStatus": (2, 2, (3, 0), (), "AudioInputInterferenceStatus", None),
		"CmdMaxAlternates": (8, 2, (3, 0), (), "CmdMaxAlternates", None),
		"EventInterests": (7, 2, (3, 0), (), "EventInterests", None),
		# Method 'Recognizer' returns object of type 'ISpeechRecognizer'
		"Recognizer": (1, 2, (9, 0), (), "Recognizer", '{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}'),
		"RequestedUIType": (3, 2, (8, 0), (), "RequestedUIType", None),
		"RetainedAudio": (10, 2, (3, 0), (), "RetainedAudio", None),
		# Method 'RetainedAudioFormat' returns object of type 'ISpeechAudioFormat'
		"RetainedAudioFormat": (11, 2, (9, 0), (), "RetainedAudioFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		"State": (9, 2, (3, 0), (), "State", None),
		# Method 'Voice' returns object of type 'ISpeechVoice'
		"Voice": (4, 2, (9, 0), (), "Voice", '{269316D8-57BD-11D2-9EEE-00C04F797396}'),
		"VoicePurgeEvent": (6, 2, (3, 0), (), "VoicePurgeEvent", None),
	}
	_prop_map_put_ = {
		"AllowVoiceFormatMatchingOnNextSet": ((5, LCID, 4, 0),()),
		"CmdMaxAlternates": ((8, LCID, 4, 0),()),
		"EventInterests": ((7, LCID, 4, 0),()),
		"RetainedAudio": ((10, LCID, 4, 0),()),
		"RetainedAudioFormat": ((11, LCID, 8, 0),()),
		"State": ((9, LCID, 4, 0),()),
		"Voice": ((4, LCID, 8, 0),()),
		"VoicePurgeEvent": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechRecoGrammar(DispatchBaseClass):
	'ISpeechRecoGrammar Interface'
	CLSID = IID('{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}')
	coclass_clsid = None

	def CmdLoadFromFile(self, FileName=defaultNamedNotOptArg, LoadOption=0):
		'CmdLoadFromFile'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (24, 0), ((8, 1), (3, 49)),FileName
			, LoadOption)

	def CmdLoadFromMemory(self, GrammarData=defaultNamedNotOptArg, LoadOption=0):
		'CmdLoadFromMemory'
		return self._oleobj_.InvokeTypes(10, LCID, 1, (24, 0), ((12, 1), (3, 49)),GrammarData
			, LoadOption)

	def CmdLoadFromObject(self, ClassId=defaultNamedNotOptArg, GrammarName=defaultNamedNotOptArg, LoadOption=0):
		'CmdLoadFromObject'
		return self._oleobj_.InvokeTypes(8, LCID, 1, (24, 0), ((8, 1), (8, 1), (3, 49)),ClassId
			, GrammarName, LoadOption)

	def CmdLoadFromProprietaryGrammar(self, ProprietaryGuid=defaultNamedNotOptArg, ProprietaryString=defaultNamedNotOptArg, ProprietaryData=defaultNamedNotOptArg, LoadOption=0):
		'CmdLoadFromProprietaryGrammar'
		return self._oleobj_.InvokeTypes(11, LCID, 1, (24, 0), ((8, 1), (8, 1), (12, 1), (3, 49)),ProprietaryGuid
			, ProprietaryString, ProprietaryData, LoadOption)

	def CmdLoadFromResource(self, hModule=defaultNamedNotOptArg, ResourceName=defaultNamedNotOptArg, ResourceType=defaultNamedNotOptArg, LanguageId=defaultNamedNotOptArg
			, LoadOption=0):
		'CmdLoadFromResource'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1), (12, 1), (12, 1), (3, 1), (3, 49)),hModule
			, ResourceName, ResourceType, LanguageId, LoadOption)

	def CmdSetRuleIdState(self, RuleId=defaultNamedNotOptArg, State=defaultNamedNotOptArg):
		'CmdSetRuleIdState'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (24, 0), ((3, 1), (3, 1)),RuleId
			, State)

	def CmdSetRuleState(self, Name=defaultNamedNotOptArg, State=defaultNamedNotOptArg):
		'CmdSetRuleState'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((8, 1), (3, 1)),Name
			, State)

	def DictationLoad(self, TopicName=u'', LoadOption=0):
		'DictationLoad'
		return self._ApplyTypes_(14, 1, (24, 32), ((8, 49), (3, 49)), u'DictationLoad', None,TopicName
			, LoadOption)

	def DictationSetState(self, State=defaultNamedNotOptArg):
		'DictationSetState'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (24, 0), ((3, 1),),State
			)

	def DictationUnload(self):
		'DictationUnload'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	def IsPronounceable(self, Word=defaultNamedNotOptArg):
		'IsPronounceable'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (3, 0), ((8, 1),),Word
			)

	def Reset(self, NewLanguage=0):
		'Reset'
		return self._oleobj_.InvokeTypes(5, LCID, 1, (24, 0), ((3, 49),),NewLanguage
			)

	def SetTextSelection(self, Info=defaultNamedNotOptArg):
		'SetTextSelection'
		return self._oleobj_.InvokeTypes(18, LCID, 1, (24, 0), ((9, 1),),Info
			)

	def SetWordSequenceData(self, Text=defaultNamedNotOptArg, TextLength=defaultNamedNotOptArg, Info=defaultNamedNotOptArg):
		'SetWordSequenceData'
		return self._oleobj_.InvokeTypes(17, LCID, 1, (24, 0), ((8, 1), (3, 1), (9, 1)),Text
			, TextLength, Info)

	_prop_map_get_ = {
		"Id": (1, 2, (12, 0), (), "Id", None),
		# Method 'RecoContext' returns object of type 'ISpeechRecoContext'
		"RecoContext": (2, 2, (9, 0), (), "RecoContext", '{580AA49D-7E1E-4809-B8E2-57DA806104B8}'),
		# Method 'Rules' returns object of type 'ISpeechGrammarRules'
		"Rules": (4, 2, (9, 0), (), "Rules", '{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}'),
		"State": (3, 2, (3, 0), (), "State", None),
	}
	_prop_map_put_ = {
		"State": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechRecoResult(DispatchBaseClass):
	'ISpeechRecoResult Interface'
	CLSID = IID('{ED2879CF-CED9-4EE6-A534-DE0191D5468D}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseAlternates
	def Alternates(self, RequestCount=defaultNamedNotOptArg, StartElement=0, Elements=-1):
		'Alternates'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((3, 1), (3, 49), (3, 49)),RequestCount
			, StartElement, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Alternates', '{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}')
		return ret

	# Result is of type ISpeechMemoryStream
	def Audio(self, StartElement=0, Elements=-1):
		'Audio'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 49), (3, 49)),StartElement
			, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Audio', '{EEB14B68-808B-4ABE-A5EA-B51DA7588008}')
		return ret

	def DiscardResultInfo(self, ValueTypes=defaultNamedNotOptArg):
		'DiscardResultInfo'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),ValueTypes
			)

	def SaveToMemory(self):
		'SaveToMemory'
		return self._ApplyTypes_(8, 1, (12, 0), (), u'SaveToMemory', None,)

	def SpeakAudio(self, StartElement=0, Elements=-1, Flags=0):
		'SpeakAudio'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 49), (3, 49), (3, 49)),StartElement
			, Elements, Flags)

	_prop_map_get_ = {
		# Method 'AudioFormat' returns object of type 'ISpeechAudioFormat'
		"AudioFormat": (3, 2, (9, 0), (), "AudioFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		# Method 'PhraseInfo' returns object of type 'ISpeechPhraseInfo'
		"PhraseInfo": (4, 2, (9, 0), (), "PhraseInfo", '{961559CF-4E67-4662-8BF0-D93F1FCD61B3}'),
		# Method 'RecoContext' returns object of type 'ISpeechRecoContext'
		"RecoContext": (1, 2, (9, 0), (), "RecoContext", '{580AA49D-7E1E-4809-B8E2-57DA806104B8}'),
		# Method 'Times' returns object of type 'ISpeechRecoResultTimes'
		"Times": (2, 2, (9, 0), (), "Times", '{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}'),
	}
	_prop_map_put_ = {
		"AudioFormat": ((3, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechRecoResult2(DispatchBaseClass):
	'ISpeechRecoResult2 Interface'
	CLSID = IID('{8E0A246D-D3C8-45DE-8657-04290C458C3C}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseAlternates
	def Alternates(self, RequestCount=defaultNamedNotOptArg, StartElement=0, Elements=-1):
		'Alternates'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((3, 1), (3, 49), (3, 49)),RequestCount
			, StartElement, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Alternates', '{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}')
		return ret

	# Result is of type ISpeechMemoryStream
	def Audio(self, StartElement=0, Elements=-1):
		'Audio'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 49), (3, 49)),StartElement
			, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Audio', '{EEB14B68-808B-4ABE-A5EA-B51DA7588008}')
		return ret

	def DiscardResultInfo(self, ValueTypes=defaultNamedNotOptArg):
		'DiscardResultInfo'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),ValueTypes
			)

	def SaveToMemory(self):
		'SaveToMemory'
		return self._ApplyTypes_(8, 1, (12, 0), (), u'SaveToMemory', None,)

	def SetTextFeedback(self, Feedback=defaultNamedNotOptArg, WasSuccessful=defaultNamedNotOptArg):
		'DiscardResultInfo'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((8, 1), (11, 1)),Feedback
			, WasSuccessful)

	def SpeakAudio(self, StartElement=0, Elements=-1, Flags=0):
		'SpeakAudio'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 49), (3, 49), (3, 49)),StartElement
			, Elements, Flags)

	_prop_map_get_ = {
		# Method 'AudioFormat' returns object of type 'ISpeechAudioFormat'
		"AudioFormat": (3, 2, (9, 0), (), "AudioFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		# Method 'PhraseInfo' returns object of type 'ISpeechPhraseInfo'
		"PhraseInfo": (4, 2, (9, 0), (), "PhraseInfo", '{961559CF-4E67-4662-8BF0-D93F1FCD61B3}'),
		# Method 'RecoContext' returns object of type 'ISpeechRecoContext'
		"RecoContext": (1, 2, (9, 0), (), "RecoContext", '{580AA49D-7E1E-4809-B8E2-57DA806104B8}'),
		# Method 'Times' returns object of type 'ISpeechRecoResultTimes'
		"Times": (2, 2, (9, 0), (), "Times", '{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}'),
	}
	_prop_map_put_ = {
		"AudioFormat": ((3, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechRecoResultDispatch(DispatchBaseClass):
	'ISpeechRecoResultDispatch Interface'
	CLSID = IID('{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseAlternates
	def Alternates(self, RequestCount=defaultNamedNotOptArg, StartElement=0, Elements=-1):
		'Alternates'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((3, 1), (3, 49), (3, 49)),RequestCount
			, StartElement, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Alternates', '{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}')
		return ret

	# Result is of type ISpeechMemoryStream
	def Audio(self, StartElement=0, Elements=-1):
		'Audio'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 49), (3, 49)),StartElement
			, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Audio', '{EEB14B68-808B-4ABE-A5EA-B51DA7588008}')
		return ret

	def DiscardResultInfo(self, ValueTypes=defaultNamedNotOptArg):
		'DiscardResultInfo'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),ValueTypes
			)

	def GetXMLErrorInfo(self, LineNumber=pythoncom.Missing, ScriptLine=pythoncom.Missing, Source=pythoncom.Missing, Description=pythoncom.Missing
			, ResultCode=pythoncom.Missing):
		'GetXMLErrorInfo'
		return self._ApplyTypes_(11, 1, (11, 0), ((16387, 2), (16392, 2), (16392, 2), (16392, 2), (16387, 2)), u'GetXMLErrorInfo', None,LineNumber
			, ScriptLine, Source, Description, ResultCode)

	def GetXMLResult(self, Options=defaultNamedNotOptArg):
		'GetXMLResult'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(10, LCID, 1, (8, 0), ((3, 1),),Options
			)

	def SaveToMemory(self):
		'SaveToMemory'
		return self._ApplyTypes_(8, 1, (12, 0), (), u'SaveToMemory', None,)

	def SetTextFeedback(self, Feedback=defaultNamedNotOptArg, WasSuccessful=defaultNamedNotOptArg):
		'SetTextFeedback'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (24, 0), ((8, 1), (11, 1)),Feedback
			, WasSuccessful)

	def SpeakAudio(self, StartElement=0, Elements=-1, Flags=0):
		'SpeakAudio'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 49), (3, 49), (3, 49)),StartElement
			, Elements, Flags)

	_prop_map_get_ = {
		# Method 'AudioFormat' returns object of type 'ISpeechAudioFormat'
		"AudioFormat": (3, 2, (9, 0), (), "AudioFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		# Method 'PhraseInfo' returns object of type 'ISpeechPhraseInfo'
		"PhraseInfo": (4, 2, (9, 0), (), "PhraseInfo", '{961559CF-4E67-4662-8BF0-D93F1FCD61B3}'),
		# Method 'RecoContext' returns object of type 'ISpeechRecoContext'
		"RecoContext": (1, 2, (9, 0), (), "RecoContext", '{580AA49D-7E1E-4809-B8E2-57DA806104B8}'),
		# Method 'Times' returns object of type 'ISpeechRecoResultTimes'
		"Times": (2, 2, (9, 0), (), "Times", '{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}'),
	}
	_prop_map_put_ = {
		"AudioFormat": ((3, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechRecoResultTimes(DispatchBaseClass):
	'ISpeechRecoResultTimes Interface'
	CLSID = IID('{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}')
	coclass_clsid = None

	_prop_map_get_ = {
		"Length": (2, 2, (12, 0), (), "Length", None),
		"OffsetFromStart": (4, 2, (12, 0), (), "OffsetFromStart", None),
		"StreamTime": (1, 2, (12, 0), (), "StreamTime", None),
		"TickCount": (3, 2, (3, 0), (), "TickCount", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechRecognizer(DispatchBaseClass):
	'ISpeechRecognizer Interface'
	CLSID = IID('{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}')
	coclass_clsid = IID('{3BEE4890-4FE9-4A37-8C1E-5E7E12791C1F}')

	# Result is of type ISpeechRecoContext
	def CreateRecoContext(self):
		'CreateRecoContext'
		ret = self._oleobj_.InvokeTypes(10, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, u'CreateRecoContext', '{580AA49D-7E1E-4809-B8E2-57DA806104B8}')
		return ret

	def DisplayUI(self, hWndParent=defaultNamedNotOptArg, Title=defaultNamedNotOptArg, TypeOfUI=defaultNamedNotOptArg, ExtraData=u''):
		'DisplayUI'
		return self._ApplyTypes_(17, 1, (24, 32), ((3, 1), (8, 1), (8, 1), (16396, 49)), u'DisplayUI', None,hWndParent
			, Title, TypeOfUI, ExtraData)

	def EmulateRecognition(self, TextElements=defaultNamedNotOptArg, ElementDisplayAttributes=u'', LanguageId=0):
		'EmulateRecognition'
		return self._ApplyTypes_(9, 1, (24, 32), ((12, 1), (16396, 49), (3, 49)), u'EmulateRecognition', None,TextElements
			, ElementDisplayAttributes, LanguageId)

	# Result is of type ISpeechObjectTokens
	def GetAudioInputs(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetAudioInputs'
		return self._ApplyTypes_(19, 1, (9, 32), ((8, 49), (8, 49)), u'GetAudioInputs', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	# Result is of type ISpeechAudioFormat
	def GetFormat(self, Type=defaultNamedNotOptArg):
		'GetFormat'
		ret = self._oleobj_.InvokeTypes(11, LCID, 1, (9, 0), ((3, 1),),Type
			)
		if ret is not None:
			ret = Dispatch(ret, u'GetFormat', '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')
		return ret

	# Result is of type ISpeechObjectTokens
	def GetProfiles(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetProfiles'
		return self._ApplyTypes_(20, 1, (9, 32), ((8, 49), (8, 49)), u'GetProfiles', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	def GetPropertyNumber(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'GetPropertyNumber'
		return self._ApplyTypes_(13, 1, (11, 0), ((8, 1), (16387, 3)), u'GetPropertyNumber', None,Name
			, Value)

	def GetPropertyString(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'GetPropertyString'
		return self._ApplyTypes_(15, 1, (11, 0), ((8, 1), (16392, 3)), u'GetPropertyString', None,Name
			, Value)

	# Result is of type ISpeechObjectTokens
	def GetRecognizers(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetRecognizers'
		return self._ApplyTypes_(18, 1, (9, 32), ((8, 49), (8, 49)), u'GetRecognizers', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	def IsUISupported(self, TypeOfUI=defaultNamedNotOptArg, ExtraData=u''):
		'IsUISupported'
		return self._ApplyTypes_(16, 1, (11, 32), ((8, 1), (16396, 49)), u'IsUISupported', None,TypeOfUI
			, ExtraData)

	def SetPropertyNumber(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'SetPropertyNumber'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (11, 0), ((8, 1), (3, 1)),Name
			, Value)

	def SetPropertyString(self, Name=defaultNamedNotOptArg, Value=defaultNamedNotOptArg):
		'SetPropertyString'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (11, 0), ((8, 1), (8, 1)),Name
			, Value)

	_prop_map_get_ = {
		"AllowAudioInputFormatChangesOnNextSet": (2, 2, (11, 0), (), "AllowAudioInputFormatChangesOnNextSet", None),
		# Method 'AudioInput' returns object of type 'ISpeechObjectToken'
		"AudioInput": (3, 2, (9, 0), (), "AudioInput", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		# Method 'AudioInputStream' returns object of type 'ISpeechBaseStream'
		"AudioInputStream": (4, 2, (9, 0), (), "AudioInputStream", '{6450336F-7D49-4CED-8097-49D6DEE37294}'),
		"IsShared": (5, 2, (11, 0), (), "IsShared", None),
		# Method 'Profile' returns object of type 'ISpeechObjectToken'
		"Profile": (8, 2, (9, 0), (), "Profile", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		# Method 'Recognizer' returns object of type 'ISpeechObjectToken'
		"Recognizer": (1, 2, (9, 0), (), "Recognizer", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		"State": (6, 2, (3, 0), (), "State", None),
		# Method 'Status' returns object of type 'ISpeechRecognizerStatus'
		"Status": (7, 2, (9, 0), (), "Status", '{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}'),
	}
	_prop_map_put_ = {
		"AllowAudioInputFormatChangesOnNextSet": ((2, LCID, 4, 0),()),
		"AudioInput": ((3, LCID, 8, 0),()),
		"AudioInputStream": ((4, LCID, 8, 0),()),
		"Profile": ((8, LCID, 8, 0),()),
		"Recognizer": ((1, LCID, 8, 0),()),
		"State": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechRecognizerStatus(DispatchBaseClass):
	'ISpeechRecognizerStatus Interface'
	CLSID = IID('{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}')
	coclass_clsid = None

	_prop_map_get_ = {
		# Method 'AudioStatus' returns object of type 'ISpeechAudioStatus'
		"AudioStatus": (1, 2, (9, 0), (), "AudioStatus", '{C62D9C91-7458-47F6-862D-1EF86FB0B278}'),
		"ClsidEngine": (5, 2, (8, 0), (), "ClsidEngine", None),
		"CurrentStreamNumber": (3, 2, (3, 0), (), "CurrentStreamNumber", None),
		"CurrentStreamPosition": (2, 2, (12, 0), (), "CurrentStreamPosition", None),
		"NumberOfActiveRules": (4, 2, (3, 0), (), "NumberOfActiveRules", None),
		"SupportedLanguages": (6, 2, (12, 0), (), "SupportedLanguages", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechResourceLoader(DispatchBaseClass):
	'ISpeechResourceLoader Interface'
	CLSID = IID('{B9AC5783-FCD0-4B21-B119-B4F8DA8FD2C3}')
	coclass_clsid = None

	def GetLocalCopy(self, bstrResourceUri=defaultNamedNotOptArg, pbstrLocalPath=pythoncom.Missing, pbstrMIMEType=pythoncom.Missing, pbstrRedirectUrl=pythoncom.Missing):
		return self._ApplyTypes_(2, 1, (24, 0), ((8, 1), (16392, 2), (16392, 2), (16392, 2)), u'GetLocalCopy', None,bstrResourceUri
			, pbstrLocalPath, pbstrMIMEType, pbstrRedirectUrl)

	def LoadResource(self, bstrResourceUri=defaultNamedNotOptArg, fAlwaysReload=defaultNamedNotOptArg, pStream=pythoncom.Missing, pbstrMIMEType=pythoncom.Missing
			, pfModified=pythoncom.Missing, pbstrRedirectUrl=pythoncom.Missing):
		return self._ApplyTypes_(1, 1, (24, 0), ((8, 1), (11, 1), (16397, 2), (16392, 2), (16395, 2), (16392, 2)), u'LoadResource', None,bstrResourceUri
			, fAlwaysReload, pStream, pbstrMIMEType, pfModified, pbstrRedirectUrl
			)

	def ReleaseLocalCopy(self, pbstrLocalPath=defaultNamedNotOptArg):
		return self._oleobj_.InvokeTypes(3, LCID, 1, (24, 0), ((8, 1),),pbstrLocalPath
			)

	_prop_map_get_ = {
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechTextSelectionInformation(DispatchBaseClass):
	'ISpeechTextSelectionInformation Interface'
	CLSID = IID('{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}')
	coclass_clsid = IID('{0F92030A-CBFD-4AB8-A164-FF5985547FF6}')

	_prop_map_get_ = {
		"ActiveLength": (2, 2, (3, 0), (), "ActiveLength", None),
		"ActiveOffset": (1, 2, (3, 0), (), "ActiveOffset", None),
		"SelectionLength": (4, 2, (3, 0), (), "SelectionLength", None),
		"SelectionOffset": (3, 2, (3, 0), (), "SelectionOffset", None),
	}
	_prop_map_put_ = {
		"ActiveLength": ((2, LCID, 4, 0),()),
		"ActiveOffset": ((1, LCID, 4, 0),()),
		"SelectionLength": ((4, LCID, 4, 0),()),
		"SelectionOffset": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechVoice(DispatchBaseClass):
	'ISpeechVoice Interface'
	CLSID = IID('{269316D8-57BD-11D2-9EEE-00C04F797396}')
	coclass_clsid = IID('{96749377-3391-11D2-9EE3-00C04F797396}')

	def DisplayUI(self, hWndParent=defaultNamedNotOptArg, Title=defaultNamedNotOptArg, TypeOfUI=defaultNamedNotOptArg, ExtraData=u''):
		'DisplayUI'
		return self._ApplyTypes_(22, 1, (24, 32), ((3, 1), (8, 1), (8, 1), (16396, 49)), u'DisplayUI', None,hWndParent
			, Title, TypeOfUI, ExtraData)

	# Result is of type ISpeechObjectTokens
	def GetAudioOutputs(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetAudioOutputs'
		return self._ApplyTypes_(18, 1, (9, 32), ((8, 49), (8, 49)), u'GetAudioOutputs', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	# Result is of type ISpeechObjectTokens
	def GetVoices(self, RequiredAttributes=u'', OptionalAttributes=u''):
		'GetVoices'
		return self._ApplyTypes_(17, 1, (9, 32), ((8, 49), (8, 49)), u'GetVoices', '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',RequiredAttributes
			, OptionalAttributes)

	def IsUISupported(self, TypeOfUI=defaultNamedNotOptArg, ExtraData=u''):
		'IsUISupported'
		return self._ApplyTypes_(21, 1, (11, 32), ((8, 1), (16396, 49)), u'IsUISupported', None,TypeOfUI
			, ExtraData)

	def Pause(self):
		'Pauses the voices rendering.'
		return self._oleobj_.InvokeTypes(14, LCID, 1, (24, 0), (),)

	def Resume(self):
		'Resumes the voices rendering.'
		return self._oleobj_.InvokeTypes(15, LCID, 1, (24, 0), (),)

	def Skip(self, Type=defaultNamedNotOptArg, NumItems=defaultNamedNotOptArg):
		'Skips rendering the specified number of items.'
		return self._oleobj_.InvokeTypes(16, LCID, 1, (3, 0), ((8, 1), (3, 1)),Type
			, NumItems)

	def Speak(self, Text=defaultNamedNotOptArg, Flags=0):
		'Speak'
		return self._oleobj_.InvokeTypes(12, LCID, 1, (3, 0), ((8, 1), (3, 49)),Text
			, Flags)

	def SpeakCompleteEvent(self):
		'SpeakCompleteEvent'
		return self._oleobj_.InvokeTypes(20, LCID, 1, (3, 0), (),)

	def SpeakStream(self, Stream=defaultNamedNotOptArg, Flags=0):
		'SpeakStream'
		return self._oleobj_.InvokeTypes(13, LCID, 1, (3, 0), ((9, 1), (3, 49)),Stream
			, Flags)

	def WaitUntilDone(self, msTimeout=defaultNamedNotOptArg):
		'WaitUntilDone'
		return self._oleobj_.InvokeTypes(19, LCID, 1, (11, 0), ((3, 1),),msTimeout
			)

	_prop_map_get_ = {
		"AlertBoundary": (10, 2, (3, 0), (), "AlertBoundary", None),
		"AllowAudioOutputFormatChangesOnNextSet": (7, 2, (11, 0), (), "AllowAudioOutputFormatChangesOnNextSet", None),
		# Method 'AudioOutput' returns object of type 'ISpeechObjectToken'
		"AudioOutput": (3, 2, (9, 0), (), "AudioOutput", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		# Method 'AudioOutputStream' returns object of type 'ISpeechBaseStream'
		"AudioOutputStream": (4, 2, (9, 0), (), "AudioOutputStream", '{6450336F-7D49-4CED-8097-49D6DEE37294}'),
		"EventInterests": (8, 2, (3, 0), (), "EventInterests", None),
		"Priority": (9, 2, (3, 0), (), "Priority", None),
		"Rate": (5, 2, (3, 0), (), "Rate", None),
		# Method 'Status' returns object of type 'ISpeechVoiceStatus'
		"Status": (1, 2, (9, 0), (), "Status", '{8BE47B07-57F6-11D2-9EEE-00C04F797396}'),
		"SynchronousSpeakTimeout": (11, 2, (3, 0), (), "SynchronousSpeakTimeout", None),
		# Method 'Voice' returns object of type 'ISpeechObjectToken'
		"Voice": (2, 2, (9, 0), (), "Voice", '{C74A3ADC-B727-4500-A84A-B526721C8B8C}'),
		"Volume": (6, 2, (3, 0), (), "Volume", None),
	}
	_prop_map_put_ = {
		"AlertBoundary": ((10, LCID, 4, 0),()),
		"AllowAudioOutputFormatChangesOnNextSet": ((7, LCID, 4, 0),()),
		"AudioOutput": ((3, LCID, 8, 0),()),
		"AudioOutputStream": ((4, LCID, 8, 0),()),
		"EventInterests": ((8, LCID, 4, 0),()),
		"Priority": ((9, LCID, 4, 0),()),
		"Rate": ((5, LCID, 4, 0),()),
		"SynchronousSpeakTimeout": ((11, LCID, 4, 0),()),
		"Voice": ((2, LCID, 8, 0),()),
		"Volume": ((6, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechVoiceStatus(DispatchBaseClass):
	'ISpeechVoiceStatus Interface'
	CLSID = IID('{8BE47B07-57F6-11D2-9EEE-00C04F797396}')
	coclass_clsid = None

	_prop_map_get_ = {
		"CurrentStreamNumber": (1, 2, (3, 0), (), "CurrentStreamNumber", None),
		"InputSentenceLength": (8, 2, (3, 0), (), "InputSentenceLength", None),
		"InputSentencePosition": (7, 2, (3, 0), (), "InputSentencePosition", None),
		"InputWordLength": (6, 2, (3, 0), (), "InputWordLength", None),
		"InputWordPosition": (5, 2, (3, 0), (), "InputWordPosition", None),
		"LastBookmark": (9, 2, (8, 0), (), "LastBookmark", None),
		"LastBookmarkId": (10, 2, (3, 0), (), "LastBookmarkId", None),
		"LastHResult": (3, 2, (3, 0), (), "LastHResult", None),
		"LastStreamNumberQueued": (2, 2, (3, 0), (), "LastStreamNumberQueued", None),
		"PhonemeId": (11, 2, (2, 0), (), "PhonemeId", None),
		"RunningState": (4, 2, (3, 0), (), "RunningState", None),
		"VisemeId": (12, 2, (2, 0), (), "VisemeId", None),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechWaveFormatEx(DispatchBaseClass):
	'ISpeechWaveFormatEx Interface'
	CLSID = IID('{7A1EF0D5-1581-4741-88E4-209A49F11A10}')
	coclass_clsid = IID('{C79A574C-63BE-44B9-801F-283F87F898BE}')

	_prop_map_get_ = {
		"AvgBytesPerSec": (4, 2, (3, 0), (), "AvgBytesPerSec", None),
		"BitsPerSample": (6, 2, (2, 0), (), "BitsPerSample", None),
		"BlockAlign": (5, 2, (2, 0), (), "BlockAlign", None),
		"Channels": (2, 2, (2, 0), (), "Channels", None),
		"ExtraData": (7, 2, (12, 0), (), "ExtraData", None),
		"FormatTag": (1, 2, (2, 0), (), "FormatTag", None),
		"SamplesPerSec": (3, 2, (3, 0), (), "SamplesPerSec", None),
	}
	_prop_map_put_ = {
		"AvgBytesPerSec": ((4, LCID, 4, 0),()),
		"BitsPerSample": ((6, LCID, 4, 0),()),
		"BlockAlign": ((5, LCID, 4, 0),()),
		"Channels": ((2, LCID, 4, 0),()),
		"ExtraData": ((7, LCID, 4, 0),()),
		"FormatTag": ((1, LCID, 4, 0),()),
		"SamplesPerSec": ((3, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISpeechXMLRecoResult(DispatchBaseClass):
	'ISpeechXMLRecoResult Interface'
	CLSID = IID('{AAEC54AF-8F85-4924-944D-B79D39D72E19}')
	coclass_clsid = None

	# Result is of type ISpeechPhraseAlternates
	def Alternates(self, RequestCount=defaultNamedNotOptArg, StartElement=0, Elements=-1):
		'Alternates'
		ret = self._oleobj_.InvokeTypes(5, LCID, 1, (9, 0), ((3, 1), (3, 49), (3, 49)),RequestCount
			, StartElement, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Alternates', '{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}')
		return ret

	# Result is of type ISpeechMemoryStream
	def Audio(self, StartElement=0, Elements=-1):
		'Audio'
		ret = self._oleobj_.InvokeTypes(6, LCID, 1, (9, 0), ((3, 49), (3, 49)),StartElement
			, Elements)
		if ret is not None:
			ret = Dispatch(ret, u'Audio', '{EEB14B68-808B-4ABE-A5EA-B51DA7588008}')
		return ret

	def DiscardResultInfo(self, ValueTypes=defaultNamedNotOptArg):
		'DiscardResultInfo'
		return self._oleobj_.InvokeTypes(9, LCID, 1, (24, 0), ((3, 1),),ValueTypes
			)

	def GetXMLErrorInfo(self, LineNumber=pythoncom.Missing, ScriptLine=pythoncom.Missing, Source=pythoncom.Missing, Description=pythoncom.Missing
			, ResultCode=pythoncom.Missing):
		'GetXMLErrorInfo'
		return self._ApplyTypes_(11, 1, (11, 0), ((16387, 2), (16392, 2), (16392, 2), (16392, 2), (16387, 2)), u'GetXMLErrorInfo', None,LineNumber
			, ScriptLine, Source, Description, ResultCode)

	def GetXMLResult(self, Options=defaultNamedNotOptArg):
		'GetXMLResult'
		# Result is a Unicode object
		return self._oleobj_.InvokeTypes(10, LCID, 1, (8, 0), ((3, 1),),Options
			)

	def SaveToMemory(self):
		'SaveToMemory'
		return self._ApplyTypes_(8, 1, (12, 0), (), u'SaveToMemory', None,)

	def SpeakAudio(self, StartElement=0, Elements=-1, Flags=0):
		'SpeakAudio'
		return self._oleobj_.InvokeTypes(7, LCID, 1, (3, 0), ((3, 49), (3, 49), (3, 49)),StartElement
			, Elements, Flags)

	_prop_map_get_ = {
		# Method 'AudioFormat' returns object of type 'ISpeechAudioFormat'
		"AudioFormat": (3, 2, (9, 0), (), "AudioFormat", '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}'),
		# Method 'PhraseInfo' returns object of type 'ISpeechPhraseInfo'
		"PhraseInfo": (4, 2, (9, 0), (), "PhraseInfo", '{961559CF-4E67-4662-8BF0-D93F1FCD61B3}'),
		# Method 'RecoContext' returns object of type 'ISpeechRecoContext'
		"RecoContext": (1, 2, (9, 0), (), "RecoContext", '{580AA49D-7E1E-4809-B8E2-57DA806104B8}'),
		# Method 'Times' returns object of type 'ISpeechRecoResultTimes'
		"Times": (2, 2, (9, 0), (), "Times", '{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}'),
	}
	_prop_map_put_ = {
		"AudioFormat": ((3, LCID, 8, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class _ISpeechRecoContextEvents:
	CLSID = CLSID_Sink = IID('{7B8FCB42-0E9D-4F00-A048-7B04D6179D3D}')
	coclass_clsid = IID('{73AD6842-ACE0-45E8-A4DD-8795881A2C2A}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		       11 : "OnFalseRecognition",
		       16 : "OnRecognitionForOtherContext",
		       18 : "OnEnginePrivate",
		       17 : "OnAudioLevel",
		        1 : "OnStartStream",
		        3 : "OnBookmark",
		       13 : "OnRequestUI",
		       12 : "OnInterference",
		        4 : "OnSoundStart",
		        2 : "OnEndStream",
		       14 : "OnRecognizerStateChange",
		        9 : "OnPropertyNumberChange",
		        8 : "OnHypothesis",
		       15 : "OnAdaptation",
		        6 : "OnPhraseStart",
		        5 : "OnSoundEnd",
		       10 : "OnPropertyStringChange",
		        7 : "OnRecognition",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnFalseRecognition(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Result=defaultNamedNotOptArg):
#		'FalseRecognition'
#	def OnRecognitionForOtherContext(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'RecognitionForOtherContext'
#	def OnEnginePrivate(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, EngineData=defaultNamedNotOptArg):
#		'EnginePrivate'
#	def OnAudioLevel(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, AudioLevel=defaultNamedNotOptArg):
#		'AudioLevel'
#	def OnStartStream(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'StartStream'
#	def OnBookmark(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, BookmarkId=defaultNamedNotOptArg, Options=defaultNamedNotOptArg):
#		'Bookmark'
#	def OnRequestUI(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, UIType=defaultNamedNotOptArg):
#		'RequestUI'
#	def OnInterference(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Interference=defaultNamedNotOptArg):
#		'Interference'
#	def OnSoundStart(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'SoundStart'
#	def OnEndStream(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, StreamReleased=defaultNamedNotOptArg):
#		'EndStream'
#	def OnRecognizerStateChange(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, NewState=defaultNamedNotOptArg):
#		'RecognizerStateChange'
#	def OnPropertyNumberChange(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, PropertyName=defaultNamedNotOptArg, NewNumberValue=defaultNamedNotOptArg):
#		'PropertyNumberChange'
#	def OnHypothesis(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Result=defaultNamedNotOptArg):
#		'Hypothesis'
#	def OnAdaptation(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'Adaptation'
#	def OnPhraseStart(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'PhraseStart'
#	def OnSoundEnd(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'SoundEnd'
#	def OnPropertyStringChange(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, PropertyName=defaultNamedNotOptArg, NewStringValue=defaultNamedNotOptArg):
#		'PropertyStringChange'
#	def OnRecognition(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, RecognitionType=defaultNamedNotOptArg, Result=defaultNamedNotOptArg):
#		'Recognition'


class _ISpeechVoiceEvents:
	CLSID = CLSID_Sink = IID('{A372ACD1-3BEF-4BBD-8FFB-CB3E2B416AF8}')
	coclass_clsid = IID('{96749377-3391-11D2-9EE3-00C04F797396}')
	_public_methods_ = [] # For COM Server support
	_dispid_to_func_ = {
		        3 : "OnVoiceChange",
		        9 : "OnAudioLevel",
		        5 : "OnWord",
		       10 : "OnEnginePrivate",
		        7 : "OnSentence",
		        4 : "OnBookmark",
		        1 : "OnStartStream",
		        2 : "OnEndStream",
		        6 : "OnPhoneme",
		        8 : "OnViseme",
		}

	def __init__(self, oobj = None):
		if oobj is None:
			self._olecp = None
		else:
			import win32com.server.util
			from win32com.server.policy import EventHandlerPolicy
			cpc=oobj._oleobj_.QueryInterface(pythoncom.IID_IConnectionPointContainer)
			cp=cpc.FindConnectionPoint(self.CLSID_Sink)
			cookie=cp.Advise(win32com.server.util.wrap(self, usePolicy=EventHandlerPolicy))
			self._olecp,self._olecp_cookie = cp,cookie
	def __del__(self):
		try:
			self.close()
		except pythoncom.com_error:
			pass
	def close(self):
		if self._olecp is not None:
			cp,cookie,self._olecp,self._olecp_cookie = self._olecp,self._olecp_cookie,None,None
			cp.Unadvise(cookie)
	def _query_interface_(self, iid):
		import win32com.server.util
		if iid==self.CLSID_Sink: return win32com.server.util.wrap(self)

	# Event Handlers
	# If you create handlers, they should have the following prototypes:
#	def OnVoiceChange(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, VoiceObjectToken=defaultNamedNotOptArg):
#		'VoiceChange'
#	def OnAudioLevel(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, AudioLevel=defaultNamedNotOptArg):
#		'AudioLevel'
#	def OnWord(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, CharacterPosition=defaultNamedNotOptArg, Length=defaultNamedNotOptArg):
#		'Word'
#	def OnEnginePrivate(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, EngineData=defaultNamedNotOptArg):
#		'EnginePrivate'
#	def OnSentence(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, CharacterPosition=defaultNamedNotOptArg, Length=defaultNamedNotOptArg):
#		'Sentence'
#	def OnBookmark(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Bookmark=defaultNamedNotOptArg, BookmarkId=defaultNamedNotOptArg):
#		'Bookmark'
#	def OnStartStream(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'StartStream'
#	def OnEndStream(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg):
#		'EndStream'
#	def OnPhoneme(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Duration=defaultNamedNotOptArg, NextPhoneId=defaultNamedNotOptArg
#			, Feature=defaultNamedNotOptArg, CurrentPhoneId=defaultNamedNotOptArg):
#		'Phoneme'
#	def OnViseme(self, StreamNumber=defaultNamedNotOptArg, StreamPosition=defaultNamedNotOptArg, Duration=defaultNamedNotOptArg, NextVisemeId=defaultNamedNotOptArg
#			, Feature=defaultNamedNotOptArg, CurrentVisemeId=defaultNamedNotOptArg):
#		'Viseme'


from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'SAPI.SpAudioFormat.1'
class SpAudioFormat(CoClassBaseClass): # A CoClass
	# SpAudioFormat Class
	CLSID = IID('{9EF96870-E160-4792-820D-48CF0649E4EC}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechAudioFormat,
	]
	default_interface = ISpeechAudioFormat

# This CoClass is known by the name 'SAPI.SpCompressedLexicon.1'
class SpCompressedLexicon(CoClassBaseClass): # A CoClass
	# SpCompressedLexicon Class
	CLSID = IID('{90903716-2F42-11D3-9C26-00C04F8EF87C}')
	coclass_sources = [
	]
	coclass_interfaces = [
	]

# This CoClass is known by the name 'SAPI.SpCustomStream.1'
class SpCustomStream(CoClassBaseClass): # A CoClass
	# SpCustomStream Class
	CLSID = IID('{8DBEF13F-1948-4AA8-8CF0-048EEBED95D8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechCustomStream,
	]
	default_interface = ISpeechCustomStream

# This CoClass is known by the name 'SAPI.SpFileStream.1'
class SpFileStream(CoClassBaseClass): # A CoClass
	# SpFileStream Class
	CLSID = IID('{947812B3-2AE1-4644-BA86-9E90DED7EC91}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechFileStream,
	]
	default_interface = ISpeechFileStream

# This CoClass is known by the name 'SAPI.SpInProcRecoContext.1'
class SpInProcRecoContext(CoClassBaseClass): # A CoClass
	# SpInProcRecoContext Class
	CLSID = IID('{73AD6842-ACE0-45E8-A4DD-8795881A2C2A}')
	coclass_sources = [
		_ISpeechRecoContextEvents,
	]
	default_source = _ISpeechRecoContextEvents
	coclass_interfaces = [
		ISpeechRecoContext,
	]
	default_interface = ISpeechRecoContext

# This CoClass is known by the name 'Sapi.SpInprocRecognizer.1'
class SpInprocRecognizer(CoClassBaseClass): # A CoClass
	# SpInprocRecognizer Class
	CLSID = IID('{41B89B6B-9399-11D2-9623-00C04F8EE628}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechRecognizer,
	]
	default_interface = ISpeechRecognizer

# This CoClass is known by the name 'SAPI.SpLexicon.1'
class SpLexicon(CoClassBaseClass): # A CoClass
	# SpLexicon Class
	CLSID = IID('{0655E396-25D0-11D3-9C26-00C04F8EF87C}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechLexicon,
	]
	default_interface = ISpeechLexicon

# This CoClass is known by the name 'SAPI.SpMMAudioEnum.1'
class SpMMAudioEnum(CoClassBaseClass): # A CoClass
	# SpMMAudioEnum Class
	CLSID = IID('{AB1890A0-E91F-11D2-BB91-00C04F8EE6C0}')
	coclass_sources = [
	]
	coclass_interfaces = [
	]

# This CoClass is known by the name 'SAPI.SpMMAudioIn.1'
class SpMMAudioIn(CoClassBaseClass): # A CoClass
	# SpMMAudioIn Class
	CLSID = IID('{CF3D2E50-53F2-11D2-960C-00C04F8EE628}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechMMSysAudio,
	]
	default_interface = ISpeechMMSysAudio

# This CoClass is known by the name 'SAPI.SpMMAudioOut.1'
class SpMMAudioOut(CoClassBaseClass): # A CoClass
	# SpMMAudioOut Class
	CLSID = IID('{A8C680EB-3D32-11D2-9EE7-00C04F797396}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechMMSysAudio,
	]
	default_interface = ISpeechMMSysAudio

# This CoClass is known by the name 'SAPI.SpMemoryStream.1'
class SpMemoryStream(CoClassBaseClass): # A CoClass
	# SpMemoryStream Class
	CLSID = IID('{5FB7EF7D-DFF4-468A-B6B7-2FCBD188F994}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechMemoryStream,
	]
	default_interface = ISpeechMemoryStream

# This CoClass is known by the name 'SAPI.SpNotifyTranslator.1'
class SpNotifyTranslator(CoClassBaseClass): # A CoClass
	# SpNotify
	CLSID = IID('{E2AE5372-5D40-11D2-960E-00C04F8EE628}')
	coclass_sources = [
	]
	coclass_interfaces = [
	]

# This CoClass is known by the name 'SAPI.SpNullPhoneConverter.1'
class SpNullPhoneConverter(CoClassBaseClass): # A CoClass
	# SpNullPhoneConverter Class
	CLSID = IID('{455F24E9-7396-4A16-9715-7C0FDBE3EFE3}')
	coclass_sources = [
	]
	coclass_interfaces = [
	]

# This CoClass is known by the name 'SAPI.SpObjectToken.1'
class SpObjectToken(CoClassBaseClass): # A CoClass
	# SpObjectToken Class
	CLSID = IID('{EF411752-3736-4CB4-9C8C-8EF4CCB58EFE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechObjectToken,
	]
	default_interface = ISpeechObjectToken

# This CoClass is known by the name 'SAPI.SpObjectTokenCategory.1'
class SpObjectTokenCategory(CoClassBaseClass): # A CoClass
	# SpObjectTokenCategory Class
	CLSID = IID('{A910187F-0C7A-45AC-92CC-59EDAFB77B53}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechObjectTokenCategory,
	]
	default_interface = ISpeechObjectTokenCategory

# This CoClass is known by the name 'SAPI.SpPhoneConverter.1'
class SpPhoneConverter(CoClassBaseClass): # A CoClass
	# SpPhoneConverter Class
	CLSID = IID('{9185F743-1143-4C28-86B5-BFF14F20E5C8}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechPhoneConverter,
	]
	default_interface = ISpeechPhoneConverter

class SpPhoneticAlphabetConverter(CoClassBaseClass): # A CoClass
	# SpPhoneticAlphabetConverter Class
	CLSID = IID('{4F414126-DFE3-4629-99EE-797978317EAD}')
	coclass_sources = [
	]
	coclass_interfaces = [
	]

# This CoClass is known by the name 'SAPI.SpPhraseInfoBuilder.1'
class SpPhraseInfoBuilder(CoClassBaseClass): # A CoClass
	# SpPhraseInfoBuilder Class
	CLSID = IID('{C23FC28D-C55F-4720-8B32-91F73C2BD5D1}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechPhraseInfoBuilder,
	]
	default_interface = ISpeechPhraseInfoBuilder

# This CoClass is known by the name 'SAPI.SpResourceManager.1'
class SpResourceManager(CoClassBaseClass): # A CoClass
	# SpResourceManger
	CLSID = IID('{96749373-3391-11D2-9EE3-00C04F797396}')
	coclass_sources = [
	]
	coclass_interfaces = [
	]

# This CoClass is known by the name 'SAPI.SpSharedRecoContext.1'
class SpSharedRecoContext(CoClassBaseClass): # A CoClass
	# SpSharedRecoContext Class
	CLSID = IID('{47206204-5ECA-11D2-960F-00C04F8EE628}')
	coclass_sources = [
		_ISpeechRecoContextEvents,
	]
	default_source = _ISpeechRecoContextEvents
	coclass_interfaces = [
		ISpeechRecoContext,
	]
	default_interface = ISpeechRecoContext

# This CoClass is known by the name 'Sapi.SpSharedRecognizer.1'
class SpSharedRecognizer(CoClassBaseClass): # A CoClass
	# SpSharedRecognizer Class
	CLSID = IID('{3BEE4890-4FE9-4A37-8C1E-5E7E12791C1F}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechRecognizer,
	]
	default_interface = ISpeechRecognizer

# This CoClass is known by the name 'SAPI.SpShortcut.1'
class SpShortcut(CoClassBaseClass): # A CoClass
	# SpShortcut Class
	CLSID = IID('{0D722F1A-9FCF-4E62-96D8-6DF8F01A26AA}')
	coclass_sources = [
	]
	coclass_interfaces = [
	]

# This CoClass is known by the name 'SAPI.SpStream.1'
class SpStream(CoClassBaseClass): # A CoClass
	# SpStream Class
	CLSID = IID('{715D9C59-4442-11D2-9605-00C04F8EE628}')
	coclass_sources = [
	]
	coclass_interfaces = [
	]

# This CoClass is known by the name 'SAPI.SpStreamFormatConverter.1'
class SpStreamFormatConverter(CoClassBaseClass): # A CoClass
	# FormatConverter Class
	CLSID = IID('{7013943A-E2EC-11D2-A086-00C04F8EF9B5}')
	coclass_sources = [
	]
	coclass_interfaces = [
	]

# This CoClass is known by the name 'SAPI.SpTextSelectionInformation.1'
class SpTextSelectionInformation(CoClassBaseClass): # A CoClass
	# SpTextSelectionInformation Class
	CLSID = IID('{0F92030A-CBFD-4AB8-A164-FF5985547FF6}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechTextSelectionInformation,
	]
	default_interface = ISpeechTextSelectionInformation

# This CoClass is known by the name 'SAPI.SpUncompressedLexicon.1'
class SpUnCompressedLexicon(CoClassBaseClass): # A CoClass
	# SpUnCompressedLexicon Class
	CLSID = IID('{C9E37C15-DF92-4727-85D6-72E5EEB6995A}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechLexicon,
	]
	default_interface = ISpeechLexicon

# This CoClass is known by the name 'SAPI.SpVoice.1'
class SpVoice(CoClassBaseClass): # A CoClass
	# SpVoice Class
	CLSID = IID('{96749377-3391-11D2-9EE3-00C04F797396}')
	coclass_sources = [
		_ISpeechVoiceEvents,
	]
	default_source = _ISpeechVoiceEvents
	coclass_interfaces = [
		ISpeechVoice,
	]
	default_interface = ISpeechVoice

# This CoClass is known by the name 'SAPI.SpWaveFormatEx.1'
class SpWaveFormatEx(CoClassBaseClass): # A CoClass
	# SpWaveFormatEx Class
	CLSID = IID('{C79A574C-63BE-44B9-801F-283F87F898BE}')
	coclass_sources = [
	]
	coclass_interfaces = [
		ISpeechWaveFormatEx,
	]
	default_interface = ISpeechWaveFormatEx

IEnumSpObjectTokens_vtables_dispatch_ = 0
IEnumSpObjectTokens_vtables_ = [
	(( u'Next' , u'celt' , u'pelt' , u'pceltFetched' , ), 1610678272, (1610678272, (), [ 
			(19, 1, None, None) , (16397, 2, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'Skip' , u'celt' , ), 1610678273, (1610678273, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Reset' , ), 1610678274, (1610678274, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Clone' , u'ppEnum' , ), 1610678275, (1610678275, (), [ (16397, 2, None, "IID('{06B64F9E-7FDA-11D2-B4F2-00C04F797396}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'ppToken' , ), 1610678276, (1610678276, (), [ (19, 1, None, None) , 
			(16397, 2, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetCount' , u'pCount' , ), 1610678277, (1610678277, (), [ (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IEnumString_vtables_dispatch_ = 0
IEnumString_vtables_ = [
	(( u'RemoteNext' , u'celt' , u'rgelt' , u'pceltFetched' , ), 1610678272, (1610678272, (), [ 
			(19, 1, None, None) , (16415, 2, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'Skip' , u'celt' , ), 1610678273, (1610678273, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'Reset' , ), 1610678274, (1610678274, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Clone' , u'ppEnum' , ), 1610678275, (1610678275, (), [ (16397, 2, None, "IID('{00000101-0000-0000-C000-000000000046}')") , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

IInternetSecurityManager_vtables_dispatch_ = 0
IInternetSecurityManager_vtables_ = [
	(( u'SetSecuritySite' , u'pSite' , ), 1610678272, (1610678272, (), [ (13, 1, None, "IID('{79EAC9ED-BAF9-11CE-8C82-00AA004BA90B}')") , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'GetSecuritySite' , u'ppSite' , ), 1610678273, (1610678273, (), [ (16397, 2, None, "IID('{79EAC9ED-BAF9-11CE-8C82-00AA004BA90B}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'MapUrlToZone' , u'pwszUrl' , u'pdwZone' , u'dwFlags' , ), 1610678274, (1610678274, (), [ 
			(31, 1, None, None) , (16403, 2, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'GetSecurityId' , u'pwszUrl' , u'pbSecurityId' , u'pcbSecurityId' , u'dwReserved' , 
			), 1610678275, (1610678275, (), [ (31, 1, None, None) , (16401, 2, None, None) , (16403, 3, None, None) , (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'ProcessUrlAction' , u'pwszUrl' , u'dwAction' , u'pPolicy' , u'cbPolicy' , 
			u'pContext' , u'cbContext' , u'dwFlags' , u'dwReserved' , ), 1610678276, (1610678276, (), [ 
			(31, 1, None, None) , (19, 1, None, None) , (16401, 2, None, None) , (19, 1, None, None) , (16401, 1, None, None) , 
			(19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'QueryCustomPolicy' , u'pwszUrl' , u'guidKey' , u'ppPolicy' , u'pcbPolicy' , 
			u'pContext' , u'cbContext' , u'dwReserved' , ), 1610678277, (1610678277, (), [ (31, 1, None, None) , 
			(36, 1, None, None) , (16401, 2, None, None) , (16403, 2, None, None) , (16401, 1, None, None) , (19, 1, None, None) , 
			(19, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetZoneMapping' , u'dwZone' , u'lpszPattern' , u'dwFlags' , ), 1610678278, (1610678278, (), [ 
			(19, 1, None, None) , (31, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetZoneMappings' , u'dwZone' , u'ppenumString' , u'dwFlags' , ), 1610678279, (1610678279, (), [ 
			(19, 1, None, None) , (16397, 2, None, "IID('{00000101-0000-0000-C000-000000000046}')") , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IInternetSecurityMgrSite_vtables_dispatch_ = 0
IInternetSecurityMgrSite_vtables_ = [
	(( u'GetWindow' , u'phwnd' , ), 1610678272, (1610678272, (), [ (36, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'EnableModeless' , u'fEnable' , ), 1610678273, (1610678273, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

ISequentialStream_vtables_dispatch_ = 0
ISequentialStream_vtables_ = [
	(( u'RemoteRead' , u'pv' , u'cb' , u'pcbRead' , ), 1610678272, (1610678272, (), [ 
			(16401, 2, None, None) , (19, 1, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'RemoteWrite' , u'pv' , u'cb' , u'pcbWritten' , ), 1610678273, (1610678273, (), [ 
			(16401, 1, None, None) , (19, 1, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

IServiceProvider_vtables_dispatch_ = 0
IServiceProvider_vtables_ = [
	(( u'RemoteQueryService' , u'guidService' , u'riid' , u'ppvObject' , ), 1610678272, (1610678272, (), [ 
			(36, 1, None, None) , (36, 1, None, None) , (16397, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
]

ISpAudio_vtables_dispatch_ = 0
ISpAudio_vtables_ = [
	(( u'SetState' , u'NewState' , u'ullReserved' , ), 1610874880, (1610874880, (), [ (3, 1, None, None) , 
			(21, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'SetFormat' , u'rguidFmtId' , u'pWaveFormatEx' , ), 1610874881, (1610874881, (), [ (36, 1, None, None) , 
			(36, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'GetStatus' , u'pStatus' , ), 1610874882, (1610874882, (), [ (36, 2, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SetBufferInfo' , u'pBuffInfo' , ), 1610874883, (1610874883, (), [ (36, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'GetBufferInfo' , u'pBuffInfo' , ), 1610874884, (1610874884, (), [ (36, 2, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'GetDefaultFormat' , u'pFormatId' , u'ppCoMemWaveFormatEx' , ), 1610874885, (1610874885, (), [ (36, 2, None, None) , 
			(16420, 2, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'EventHandle' , ), 1610874886, (1610874886, (), [ ], 1 , 1 , 4 , 0 , 168 , (16408, 0, None, None) , 0 , )),
	(( u'GetVolumeLevel' , u'pLevel' , ), 1610874887, (1610874887, (), [ (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'SetVolumeLevel' , u'Level' , ), 1610874888, (1610874888, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'GetBufferNotifySize' , u'pcbSize' , ), 1610874889, (1610874889, (), [ (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'SetBufferNotifySize' , u'cbSize' , ), 1610874890, (1610874890, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ISpDataKey_vtables_dispatch_ = 0
ISpDataKey_vtables_ = [
	(( u'SetData' , u'pszValueName' , u'cbData' , u'pData' , ), 1610678272, (1610678272, (), [ 
			(31, 0, None, None) , (19, 0, None, None) , (16401, 0, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'GetData' , u'pszValueName' , u'pcbData' , u'pData' , ), 1610678273, (1610678273, (), [ 
			(31, 0, None, None) , (16403, 0, None, None) , (16401, 0, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'SetStringValue' , u'pszValueName' , u'pszValue' , ), 1610678274, (1610678274, (), [ (31, 1, None, None) , 
			(31, 0, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'GetStringValue' , u'pszValueName' , u'ppszValue' , ), 1610678275, (1610678275, (), [ (31, 1, None, None) , 
			(16415, 2, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'SetDWORD' , u'pszValueName' , u'dwValue' , ), 1610678276, (1610678276, (), [ (31, 0, None, None) , 
			(19, 0, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetDWORD' , u'pszValueName' , u'pdwValue' , ), 1610678277, (1610678277, (), [ (31, 0, None, None) , 
			(16403, 0, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'OpenKey' , u'pszSubKeyName' , u'ppSubKey' , ), 1610678278, (1610678278, (), [ (31, 0, None, None) , 
			(16397, 0, None, "IID('{14056581-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'CreateKey' , u'pszSubKey' , u'ppSubKey' , ), 1610678279, (1610678279, (), [ (31, 0, None, None) , 
			(16397, 0, None, "IID('{14056581-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'DeleteKey' , u'pszSubKey' , ), 1610678280, (1610678280, (), [ (31, 0, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'DeleteValue' , u'pszValueName' , ), 1610678281, (1610678281, (), [ (31, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'EnumKeys' , u'Index' , u'ppszSubKeyName' , ), 1610678282, (1610678282, (), [ (19, 0, None, None) , 
			(16415, 2, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'EnumValues' , u'Index' , u'ppszValueName' , ), 1610678283, (1610678283, (), [ (19, 0, None, None) , 
			(16415, 2, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISpEventSink_vtables_dispatch_ = 0
ISpEventSink_vtables_ = [
	(( u'AddEvents' , u'pEventArray' , u'ulCount' , ), 1610678272, (1610678272, (), [ (36, 1, None, None) , 
			(19, 1, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'GetEventInterest' , u'pullEventInterest' , ), 1610678273, (1610678273, (), [ (16405, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

ISpEventSource_vtables_dispatch_ = 0
ISpEventSource_vtables_ = [
	(( u'SetInterest' , u'ullEventInterest' , u'ullQueuedInterest' , ), 1610743808, (1610743808, (), [ (21, 1, None, None) , 
			(21, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetEvents' , u'ulCount' , u'pEventArray' , u'pulFetched' , ), 1610743809, (1610743809, (), [ 
			(19, 1, None, None) , (36, 2, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'GetInfo' , u'pInfo' , ), 1610743810, (1610743810, (), [ (36, 2, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ISpGrammarBuilder_vtables_dispatch_ = 0
ISpGrammarBuilder_vtables_ = [
	(( u'ResetGrammar' , u'NewLanguage' , ), 1610678272, (1610678272, (), [ (18, 1, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'GetRule' , u'pszRuleName' , u'dwRuleId' , u'dwAttributes' , u'fCreateIfNotExist' , 
			u'phInitialState' , ), 1610678273, (1610678273, (), [ (31, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , 
			(3, 1, None, None) , (16408, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ClearRule' , u'hState' , ), 1610678274, (1610678274, (), [ (16408, 0, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'CreateNewState' , u'hState' , u'phState' , ), 1610678275, (1610678275, (), [ (16408, 0, None, None) , 
			(16408, 0, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'AddWordTransition' , u'hFromState' , u'hToState' , u'psz' , u'pszSeparators' , 
			u'eWordType' , u'Weight' , u'pPropInfo' , ), 1610678276, (1610678276, (), [ (16408, 0, None, None) , 
			(16408, 0, None, None) , (31, 0, None, None) , (31, 0, None, None) , (3, 0, None, None) , (4, 0, None, None) , 
			(36, 0, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'AddRuleTransition' , u'hFromState' , u'hToState' , u'hRule' , u'Weight' , 
			u'pPropInfo' , ), 1610678277, (1610678277, (), [ (16408, 0, None, None) , (16408, 0, None, None) , (16408, 0, None, None) , 
			(4, 0, None, None) , (36, 0, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AddResource' , u'hRuleState' , u'pszResourceName' , u'pszResourceValue' , ), 1610678278, (1610678278, (), [ 
			(16408, 1, None, None) , (31, 1, None, None) , (31, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Commit' , u'dwReserved' , ), 1610678279, (1610678279, (), [ (19, 0, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISpLexicon_vtables_dispatch_ = 0
ISpLexicon_vtables_ = [
	(( u'GetPronunciations' , u'pszWord' , u'LangId' , u'dwFlags' , u'pWordPronunciationList' , 
			), 1610678272, (1610678272, (), [ (31, 1, None, None) , (18, 1, None, None) , (19, 1, None, None) , (36, 3, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'AddPronunciation' , u'pszWord' , u'LangId' , u'ePartOfSpeech' , u'pszPronunciation' , 
			), 1610678273, (1610678273, (), [ (31, 1, None, None) , (18, 1, None, None) , (3, 1, None, None) , (31, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'RemovePronunciation' , u'pszWord' , u'LangId' , u'ePartOfSpeech' , u'pszPronunciation' , 
			), 1610678274, (1610678274, (), [ (31, 1, None, None) , (18, 1, None, None) , (3, 1, None, None) , (31, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'GetGeneration' , u'pdwGeneration' , ), 1610678275, (1610678275, (), [ (16403, 0, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'GetGenerationChange' , u'dwFlags' , u'pdwGeneration' , u'pWordList' , ), 1610678276, (1610678276, (), [ 
			(19, 1, None, None) , (16403, 3, None, None) , (36, 3, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetWords' , u'dwFlags' , u'pdwGeneration' , u'pdwCookie' , u'pWordList' , 
			), 1610678277, (1610678277, (), [ (19, 1, None, None) , (16403, 3, None, None) , (16403, 3, None, None) , (36, 3, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISpMMSysAudio_vtables_dispatch_ = 0
ISpMMSysAudio_vtables_ = [
	(( u'GetDeviceId' , u'puDeviceId' , ), 1610940416, (1610940416, (), [ (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'SetDeviceId' , u'uDeviceId' , ), 1610940417, (1610940417, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'GetMMHandle' , u'pHandle' , ), 1610940418, (1610940418, (), [ (16408, 0, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'GetLineId' , u'puLineId' , ), 1610940419, (1610940419, (), [ (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'SetLineId' , u'uLineId' , ), 1610940420, (1610940420, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

ISpNotifySink_vtables_dispatch_ = 0
ISpNotifySink_vtables_ = [
	(( u'Notify' , ), 1610678272, (1610678272, (), [ ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
]

ISpNotifySource_vtables_dispatch_ = 0
ISpNotifySource_vtables_ = [
	(( u'SetNotifySink' , u'pNotifySink' , ), 1610678272, (1610678272, (), [ (13, 1, None, "IID('{259684DC-37C3-11D2-9603-00C04F8EE628}')") , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'SetNotifyWindowMessage' , u'hWnd' , u'Msg' , u'wParam' , u'lParam' , 
			), 1610678273, (1610678273, (), [ (36, 1, None, None) , (19, 1, None, None) , (21, 1, None, None) , (20, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'SetNotifyCallbackFunction' , u'pfnCallback' , u'wParam' , u'lParam' , ), 1610678274, (1610678274, (), [ 
			(16408, 1, None, None) , (21, 1, None, None) , (20, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'SetNotifyCallbackInterface' , u'pSpCallback' , u'wParam' , u'lParam' , ), 1610678275, (1610678275, (), [ 
			(16408, 1, None, None) , (21, 1, None, None) , (20, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'SetNotifyWin32Event' , ), 1610678276, (1610678276, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'WaitForNotifyEvent' , u'dwMilliseconds' , ), 1610678277, (1610678277, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GetNotifyEventHandle' , ), 1610678278, (1610678278, (), [ ], 1 , 1 , 4 , 0 , 72 , (16408, 0, None, None) , 0 , )),
]

ISpNotifyTranslator_vtables_dispatch_ = 0
ISpNotifyTranslator_vtables_ = [
	(( u'InitWindowMessage' , u'hWnd' , u'Msg' , u'wParam' , u'lParam' , 
			), 1610743808, (1610743808, (), [ (36, 1, None, None) , (19, 1, None, None) , (21, 1, None, None) , (20, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'InitCallback' , u'pfnCallback' , u'wParam' , u'lParam' , ), 1610743809, (1610743809, (), [ 
			(16408, 1, None, None) , (21, 1, None, None) , (20, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'InitSpNotifyCallback' , u'pSpCallback' , u'wParam' , u'lParam' , ), 1610743810, (1610743810, (), [ 
			(16408, 1, None, None) , (21, 1, None, None) , (20, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'InitWin32Event' , u'hEvent' , u'fCloseHandleOnRelease' , ), 1610743811, (1610743811, (), [ (16408, 0, None, None) , 
			(3, 0, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Wait' , u'dwMilliseconds' , ), 1610743812, (1610743812, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GetEventHandle' , ), 1610743813, (1610743813, (), [ ], 1 , 1 , 4 , 0 , 72 , (16408, 0, None, None) , 0 , )),
]

ISpObjectToken_vtables_dispatch_ = 0
ISpObjectToken_vtables_ = [
	(( u'SetId' , u'pszCategoryId' , u'pszTokenId' , u'fCreateIfNotExist' , ), 1610743808, (1610743808, (), [ 
			(31, 0, None, None) , (31, 0, None, None) , (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'GetId' , u'ppszCoMemTokenId' , ), 1610743809, (1610743809, (), [ (16415, 2, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'GetCategory' , u'ppTokenCategory' , ), 1610743810, (1610743810, (), [ (16397, 0, None, "IID('{2D3D3845-39AF-4850-BBF9-40B49780011D}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'CreateInstance' , u'pUnkOuter' , u'dwClsContext' , u'riid' , u'ppvObject' , 
			), 1610743811, (1610743811, (), [ (13, 1, None, None) , (19, 1, None, None) , (36, 1, None, None) , (16408, 2, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'GetStorageFileName' , u'clsidCaller' , u'pszValueName' , u'pszFileNameSpecifier' , u'nFolder' , 
			u'ppszFilePath' , ), 1610743812, (1610743812, (), [ (36, 1, None, None) , (31, 1, None, None) , (31, 1, None, None) , 
			(19, 1, None, None) , (16415, 2, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'RemoveStorageFileName' , u'clsidCaller' , u'pszKeyName' , u'fDeleteFile' , ), 1610743813, (1610743813, (), [ 
			(36, 1, None, None) , (31, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'Remove' , u'pclsidCaller' , ), 1610743814, (1610743814, (), [ (36, 0, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'IsUISupported' , u'pszTypeOfUI' , u'pvExtraData' , u'cbExtraData' , u'punkObject' , 
			u'pfSupported' , ), 1610743815, (1610743815, (), [ (31, 1, None, None) , (16408, 1, None, None) , (19, 1, None, None) , 
			(13, 1, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'DisplayUI' , u'hWndParent' , u'pszTitle' , u'pszTypeOfUI' , u'pvExtraData' , 
			u'cbExtraData' , u'punkObject' , ), 1610743816, (1610743816, (), [ (36, 1, None, None) , (31, 1, None, None) , 
			(31, 1, None, None) , (16408, 1, None, None) , (19, 1, None, None) , (13, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'MatchesAttributes' , u'pszAttributes' , u'pfMatches' , ), 1610743817, (1610743817, (), [ (31, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

ISpObjectTokenCategory_vtables_dispatch_ = 0
ISpObjectTokenCategory_vtables_ = [
	(( u'SetId' , u'pszCategoryId' , u'fCreateIfNotExist' , ), 1610743808, (1610743808, (), [ (31, 1, None, None) , 
			(3, 0, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'GetId' , u'ppszCoMemCategoryId' , ), 1610743809, (1610743809, (), [ (16415, 2, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'GetDataKey' , u'spdkl' , u'ppDataKey' , ), 1610743810, (1610743810, (), [ (3, 0, None, None) , 
			(16397, 0, None, "IID('{14056581-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'EnumTokens' , u'pzsReqAttribs' , u'pszOptAttribs' , u'ppEnum' , ), 1610743811, (1610743811, (), [ 
			(31, 1, None, None) , (31, 1, None, None) , (16397, 2, None, "IID('{06B64F9E-7FDA-11D2-B4F2-00C04F797396}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'SetDefaultTokenId' , u'pszTokenId' , ), 1610743812, (1610743812, (), [ (31, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'GetDefaultTokenId' , u'ppszCoMemTokenId' , ), 1610743813, (1610743813, (), [ (16415, 2, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

ISpObjectWithToken_vtables_dispatch_ = 0
ISpObjectWithToken_vtables_ = [
	(( u'SetObjectToken' , u'pToken' , ), 1610678272, (1610678272, (), [ (13, 0, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'GetObjectToken' , u'ppToken' , ), 1610678273, (1610678273, (), [ (16397, 0, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

ISpPhoneConverter_vtables_dispatch_ = 0
ISpPhoneConverter_vtables_ = [
	(( u'PhoneToId' , u'pszPhone' , u'pId' , ), 1610743808, (1610743808, (), [ (31, 1, None, None) , 
			(16402, 2, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'IdToPhone' , u'pId' , u'pszPhone' , ), 1610743809, (1610743809, (), [ (31, 1, None, None) , 
			(16402, 2, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ISpPhoneticAlphabetConverter_vtables_dispatch_ = 0
ISpPhoneticAlphabetConverter_vtables_ = [
	(( u'GetLangId' , u'pLangID' , ), 1610678272, (1610678272, (), [ (16402, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'SetLangId' , u'LangId' , ), 1610678273, (1610678273, (), [ (18, 0, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'SAPI2UPS' , u'pszSAPIId' , u'pszUPSId' , u'cMaxLength' , ), 1610678274, (1610678274, (), [ 
			(16402, 1, None, None) , (16402, 2, None, None) , (19, 0, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'UPS2SAPI' , u'pszUPSId' , u'pszSAPIId' , u'cMaxLength' , ), 1610678275, (1610678275, (), [ 
			(16402, 1, None, None) , (16402, 2, None, None) , (19, 0, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'GetMaxConvertLength' , u'cSrcLength' , u'bSAPI2UPS' , u'pcMaxDestLength' , ), 1610678276, (1610678276, (), [ 
			(19, 0, None, None) , (3, 0, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

ISpPhoneticAlphabetSelection_vtables_dispatch_ = 0
ISpPhoneticAlphabetSelection_vtables_ = [
	(( u'IsAlphabetUPS' , u'pfIsUPS' , ), 1610678272, (1610678272, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'SetAlphabetToUPS' , u'fForceUPS' , ), 1610678273, (1610678273, (), [ (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

ISpPhrase_vtables_dispatch_ = 0
ISpPhrase_vtables_ = [
	(( u'GetPhrase' , u'ppCoMemPhrase' , ), 1610678272, (1610678272, (), [ (16420, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'GetSerializedPhrase' , u'ppCoMemPhrase' , ), 1610678273, (1610678273, (), [ (16420, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetText' , u'ulStart' , u'ulCount' , u'fUseTextReplacements' , u'ppszCoMemText' , 
			u'pbDisplayAttributes' , ), 1610678274, (1610678274, (), [ (19, 1, None, None) , (19, 1, None, None) , (3, 1, None, None) , 
			(16415, 2, None, None) , (16401, 18, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'Discard' , u'dwValueTypes' , ), 1610678275, (1610678275, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ISpPhraseAlt_vtables_dispatch_ = 0
ISpPhraseAlt_vtables_ = [
	(( u'GetAltInfo' , u'ppParent' , u'pulStartElementInParent' , u'pcElementsInParent' , u'pcElementsInAlt' , 
			), 1610743808, (1610743808, (), [ (16397, 0, None, "IID('{1A5C0354-B621-4B5A-8791-D306ED379E53}')") , (16403, 0, None, None) , (16403, 0, None, None) , (16403, 0, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Commit' , ), 1610743809, (1610743809, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ISpProperties_vtables_dispatch_ = 0
ISpProperties_vtables_ = [
	(( u'SetPropertyNum' , u'pName' , u'lValue' , ), 1610678272, (1610678272, (), [ (31, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'GetPropertyNum' , u'pName' , u'plValue' , ), 1610678273, (1610678273, (), [ (31, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'SetPropertyString' , u'pName' , u'pValue' , ), 1610678274, (1610678274, (), [ (31, 1, None, None) , 
			(31, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'GetPropertyString' , u'pName' , u'ppCoMemValue' , ), 1610678275, (1610678275, (), [ (31, 1, None, None) , 
			(16415, 2, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
]

ISpRecoCategory_vtables_dispatch_ = 0
ISpRecoCategory_vtables_ = [
	(( u'GetType' , u'peCategoryType' , ), 1610678272, (1610678272, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
]

ISpRecoContext_vtables_dispatch_ = 0
ISpRecoContext_vtables_ = [
	(( u'GetRecognizer' , u'ppRecognizer' , ), 1610809344, (1610809344, (), [ (16397, 2, None, "IID('{C2B5F241-DAA0-4507-9E16-5A1EAA2B7A5C}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'CreateGrammar' , u'ullGrammarID' , u'ppGrammar' , ), 1610809345, (1610809345, (), [ (21, 1, None, None) , 
			(16397, 2, None, "IID('{2177DB29-7F45-47D0-8554-067E91C80502}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'GetStatus' , u'pStatus' , ), 1610809346, (1610809346, (), [ (36, 2, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'GetMaxAlternates' , u'pcAlternates' , ), 1610809347, (1610809347, (), [ (16403, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'SetMaxAlternates' , u'cAlternates' , ), 1610809348, (1610809348, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SetAudioOptions' , u'Options' , u'pAudioFormatId' , u'pWaveFormatEx' , ), 1610809349, (1610809349, (), [ 
			(3, 1, None, None) , (36, 1, None, None) , (36, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'GetAudioOptions' , u'pOptions' , u'pAudioFormatId' , u'ppCoMemWFEX' , ), 1610809350, (1610809350, (), [ 
			(16387, 1, None, None) , (36, 2, None, None) , (16420, 2, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'DeserializeResult' , u'pSerializedResult' , u'ppResult' , ), 1610809351, (1610809351, (), [ (36, 1, None, None) , 
			(16397, 2, None, "IID('{20B053BE-E235-43CD-9A2A-8D17A48B7842}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'Bookmark' , u'Options' , u'ullStreamPosition' , u'lparamEvent' , ), 1610809352, (1610809352, (), [ 
			(3, 1, None, None) , (21, 1, None, None) , (20, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'SetAdaptationData' , u'pAdaptationData' , u'cch' , ), 1610809353, (1610809353, (), [ (31, 1, None, None) , 
			(19, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'Pause' , u'dwReserved' , ), 1610809354, (1610809354, (), [ (19, 0, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'Resume' , u'dwReserved' , ), 1610809355, (1610809355, (), [ (19, 0, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'SetVoice' , u'pVoice' , u'fAllowFormatChanges' , ), 1610809356, (1610809356, (), [ (13, 1, None, "IID('{6C44DF74-72B9-4992-A1EC-EF996E0422D4}')") , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'GetVoice' , u'ppVoice' , ), 1610809357, (1610809357, (), [ (16397, 2, None, "IID('{6C44DF74-72B9-4992-A1EC-EF996E0422D4}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'SetVoicePurgeEvent' , u'ullEventInterest' , ), 1610809358, (1610809358, (), [ (21, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'GetVoicePurgeEvent' , u'pullEventInterest' , ), 1610809359, (1610809359, (), [ (16405, 2, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'SetContextState' , u'eContextState' , ), 1610809360, (1610809360, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'GetContextState' , u'peContextState' , ), 1610809361, (1610809361, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

ISpRecoContext2_vtables_dispatch_ = 0
ISpRecoContext2_vtables_ = [
	(( u'SetGrammarOptions' , u'eGrammarOptions' , ), 1610678272, (1610678272, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'GetGrammarOptions' , u'peGrammarOptions' , ), 1610678273, (1610678273, (), [ (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'SetAdaptationData2' , u'pAdaptationData' , u'cch' , u'pTopicName' , u'eAdaptationSettings' , 
			u'eRelevance' , ), 1610678274, (1610678274, (), [ (31, 1, None, None) , (19, 0, None, None) , (31, 1, None, None) , 
			(19, 0, None, None) , (3, 0, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

ISpRecoGrammar_vtables_dispatch_ = 0
ISpRecoGrammar_vtables_ = [
	(( u'GetGrammarId' , u'pullGrammarId' , ), 1610743808, (1610743808, (), [ (16405, 2, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'GetRecoContext' , u'ppRecoCtxt' , ), 1610743809, (1610743809, (), [ (16397, 2, None, "IID('{F740A62F-7C15-489E-8234-940A33D9272D}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'LoadCmdFromFile' , u'pszFileName' , u'Options' , ), 1610743810, (1610743810, (), [ (31, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'LoadCmdFromObject' , u'rcid' , u'pszGrammarName' , u'Options' , ), 1610743811, (1610743811, (), [ 
			(36, 1, None, None) , (31, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'LoadCmdFromResource' , u'hModule' , u'pszResourceName' , u'pszResourceType' , u'wLanguage' , 
			u'Options' , ), 1610743812, (1610743812, (), [ (16408, 1, None, None) , (31, 1, None, None) , (31, 1, None, None) , 
			(18, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'LoadCmdFromMemory' , u'pGrammar' , u'Options' , ), 1610743813, (1610743813, (), [ (36, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'LoadCmdFromProprietaryGrammar' , u'rguidParam' , u'pszStringParam' , u'pvDataPrarm' , u'cbDataSize' , 
			u'Options' , ), 1610743814, (1610743814, (), [ (36, 1, None, None) , (31, 1, None, None) , (16408, 1, None, None) , 
			(19, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SetRuleState' , u'pszName' , u'pReserved' , u'NewState' , ), 1610743815, (1610743815, (), [ 
			(31, 1, None, None) , (16408, 0, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'SetRuleIdState' , u'ulRuleId' , u'NewState' , ), 1610743816, (1610743816, (), [ (19, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'LoadDictation' , u'pszTopicName' , u'Options' , ), 1610743817, (1610743817, (), [ (31, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'UnloadDictation' , ), 1610743818, (1610743818, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'SetDictationState' , u'NewState' , ), 1610743819, (1610743819, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'SetWordSequenceData' , u'pText' , u'cchText' , u'pInfo' , ), 1610743820, (1610743820, (), [ 
			(16402, 1, None, None) , (19, 1, None, None) , (36, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'SetTextSelection' , u'pInfo' , ), 1610743821, (1610743821, (), [ (36, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'IsPronounceable' , u'pszWord' , u'pWordPronounceable' , ), 1610743822, (1610743822, (), [ (31, 1, None, None) , 
			(16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'SetGrammarState' , u'eGrammarState' , ), 1610743823, (1610743823, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'SaveCmd' , u'pStream' , u'ppszCoMemErrorText' , ), 1610743824, (1610743824, (), [ (13, 1, None, "IID('{0000000C-0000-0000-C000-000000000046}')") , 
			(16415, 18, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'GetGrammarState' , u'peGrammarState' , ), 1610743825, (1610743825, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

ISpRecoGrammar2_vtables_dispatch_ = 0
ISpRecoGrammar2_vtables_ = [
	(( u'GetRules' , u'ppCoMemRules' , u'puNumRules' , ), 1610678272, (1610678272, (), [ (16420, 2, None, None) , 
			(16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'LoadCmdFromFile2' , u'pszFileName' , u'Options' , u'pszSharingUri' , u'pszBaseUri' , 
			), 1610678273, (1610678273, (), [ (31, 1, None, None) , (3, 1, None, None) , (31, 1, None, None) , (31, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'LoadCmdFromMemory2' , u'pGrammar' , u'Options' , u'pszSharingUri' , u'pszBaseUri' , 
			), 1610678274, (1610678274, (), [ (36, 1, None, None) , (3, 1, None, None) , (31, 1, None, None) , (31, 1, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'SetRulePriority' , u'pszRuleName' , u'ulRuleId' , u'nRulePriority' , ), 1610678275, (1610678275, (), [ 
			(31, 1, None, None) , (19, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'SetRuleWeight' , u'pszRuleName' , u'ulRuleId' , u'flWeight' , ), 1610678276, (1610678276, (), [ 
			(31, 1, None, None) , (19, 1, None, None) , (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'SetDictationWeight' , u'flWeight' , ), 1610678277, (1610678277, (), [ (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetGrammarLoader' , u'pLoader' , ), 1610678278, (1610678278, (), [ (9, 1, None, "IID('{B9AC5783-FCD0-4B21-B119-B4F8DA8FD2C3}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SetSMLSecurityManager' , u'pSMLSecurityManager' , ), 1610678279, (1610678279, (), [ (13, 1, None, "IID('{79EAC9EE-BAF9-11CE-8C82-00AA004BA90B}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISpRecoResult_vtables_dispatch_ = 0
ISpRecoResult_vtables_ = [
	(( u'GetResultTimes' , u'pTimes' , ), 1610743808, (1610743808, (), [ (36, 2, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetAlternates' , u'ulStartElement' , u'cElements' , u'ulRequestCount' , u'ppPhrases' , 
			u'pcPhrasesReturned' , ), 1610743809, (1610743809, (), [ (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , 
			(16397, 2, None, "IID('{8FCEBC98-4E49-4067-9C6C-D86A0E092E3D}')") , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GetAudio' , u'ulStartElement' , u'cElements' , u'ppStream' , ), 1610743810, (1610743810, (), [ 
			(19, 1, None, None) , (19, 1, None, None) , (16397, 2, None, "IID('{BED530BE-2606-4F4D-A1C0-54C5CDA5566F}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SpeakAudio' , u'ulStartElement' , u'cElements' , u'dwFlags' , u'pulStreamNumber' , 
			), 1610743811, (1610743811, (), [ (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Serialize' , u'ppCoMemSerializedResult' , ), 1610743812, (1610743812, (), [ (16420, 2, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'ScaleAudio' , u'pAudioFormatId' , u'pWaveFormatEx' , ), 1610743813, (1610743813, (), [ (36, 1, None, None) , 
			(36, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'GetRecoContext' , u'ppRecoContext' , ), 1610743814, (1610743814, (), [ (16397, 2, None, "IID('{F740A62F-7C15-489E-8234-940A33D9272D}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISpRecognizer_vtables_dispatch_ = 0
ISpRecognizer_vtables_ = [
	(( u'SetRecognizer' , u'pRecognizer' , ), 1610743808, (1610743808, (), [ (13, 1, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetRecognizer' , u'ppRecognizer' , ), 1610743809, (1610743809, (), [ (16397, 2, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetInput' , u'pUnkInput' , u'fAllowFormatChanges' , ), 1610743810, (1610743810, (), [ (13, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetInputObjectToken' , u'ppToken' , ), 1610743811, (1610743811, (), [ (16397, 2, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetInputStream' , u'ppStream' , ), 1610743812, (1610743812, (), [ (16397, 2, None, "IID('{BED530BE-2606-4F4D-A1C0-54C5CDA5566F}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'CreateRecoContext' , u'ppNewCtxt' , ), 1610743813, (1610743813, (), [ (16397, 2, None, "IID('{F740A62F-7C15-489E-8234-940A33D9272D}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'GetRecoProfile' , u'ppToken' , ), 1610743814, (1610743814, (), [ (16397, 2, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'SetRecoProfile' , u'pToken' , ), 1610743815, (1610743815, (), [ (13, 1, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'IsSharedInstance' , ), 1610743816, (1610743816, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'GetRecoState' , u'pState' , ), 1610743817, (1610743817, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'SetRecoState' , u'NewState' , ), 1610743818, (1610743818, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'GetStatus' , u'pStatus' , ), 1610743819, (1610743819, (), [ (36, 2, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'GetFormat' , u'WaveFormatType' , u'pFormatId' , u'ppCoMemWFEX' , ), 1610743820, (1610743820, (), [ 
			(3, 1, None, None) , (36, 2, None, None) , (16420, 2, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'IsUISupported' , u'pszTypeOfUI' , u'pvExtraData' , u'cbExtraData' , u'pfSupported' , 
			), 1610743821, (1610743821, (), [ (31, 1, None, None) , (16408, 1, None, None) , (19, 1, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'DisplayUI' , u'hWndParent' , u'pszTitle' , u'pszTypeOfUI' , u'pvExtraData' , 
			u'cbExtraData' , ), 1610743822, (1610743822, (), [ (36, 1, None, None) , (31, 1, None, None) , (31, 1, None, None) , 
			(16408, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'EmulateRecognition' , u'pPhrase' , ), 1610743823, (1610743823, (), [ (13, 1, None, "IID('{1A5C0354-B621-4B5A-8791-D306ED379E53}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

ISpRecognizer2_vtables_dispatch_ = 0
ISpRecognizer2_vtables_ = [
	(( u'EmulateRecognitionEx' , u'pPhrase' , u'dwCompareFlags' , ), 1610678272, (1610678272, (), [ (13, 1, None, "IID('{1A5C0354-B621-4B5A-8791-D306ED379E53}')") , 
			(19, 1, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'SetTrainingState' , u'fDoingTraining' , u'fAdaptFromTrainingData' , ), 1610678273, (1610678273, (), [ (3, 0, None, None) , 
			(3, 0, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'ResetAcousticModelAdaptation' , ), 1610678274, (1610678274, (), [ ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

ISpRecognizer3_vtables_dispatch_ = 0
ISpRecognizer3_vtables_ = [
	(( u'GetCategory' , u'categoryType' , u'ppCategory' , ), 1610678272, (1610678272, (), [ (3, 1, None, None) , 
			(16397, 2, None, "IID('{DA0CD0F9-14A2-4F09-8C2A-85CC48979345}')") , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'SetActiveCategory' , u'pCategory' , ), 1610678273, (1610678273, (), [ (13, 1, None, "IID('{DA0CD0F9-14A2-4F09-8C2A-85CC48979345}')") , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetActiveCategory' , u'ppCategory' , ), 1610678274, (1610678274, (), [ (16397, 2, None, "IID('{DA0CD0F9-14A2-4F09-8C2A-85CC48979345}')") , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

ISpResourceManager_vtables_dispatch_ = 0
ISpResourceManager_vtables_ = [
	(( u'SetObject' , u'guidServiceId' , u'punkObject' , ), 1610743808, (1610743808, (), [ (36, 1, None, None) , 
			(13, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetObject' , u'guidServiceId' , u'ObjectCLSID' , u'ObjectIID' , u'fReleaseWhenLastExternalRefReleased' , 
			u'ppObject' , ), 1610743809, (1610743809, (), [ (36, 1, None, None) , (36, 1, None, None) , (36, 1, None, None) , 
			(3, 1, None, None) , (16408, 2, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
]

ISpSerializeState_vtables_dispatch_ = 0
ISpSerializeState_vtables_ = [
	(( u'GetSerializedState' , u'ppbData' , u'pulSize' , u'dwReserved' , ), 1610678272, (1610678272, (), [ 
			(16401, 2, None, None) , (16403, 2, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'SetSerializedState' , u'pbData' , u'ulSize' , u'dwReserved' , ), 1610678273, (1610678273, (), [ 
			(16401, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
]

ISpShortcut_vtables_dispatch_ = 0
ISpShortcut_vtables_ = [
	(( u'AddShortcut' , u'pszDisplay' , u'LangId' , u'pszSpoken' , u'shType' , 
			), 1610678272, (1610678272, (), [ (31, 1, None, None) , (18, 1, None, None) , (31, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 24 , (3, 0, None, None) , 0 , )),
	(( u'RemoveShortcut' , u'pszDisplay' , u'LangId' , u'pszSpoken' , u'shType' , 
			), 1610678273, (1610678273, (), [ (31, 1, None, None) , (18, 1, None, None) , (31, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 32 , (3, 0, None, None) , 0 , )),
	(( u'GetShortcuts' , u'LangId' , u'pShortcutpairList' , ), 1610678274, (1610678274, (), [ (18, 1, None, None) , 
			(36, 3, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'GetGeneration' , u'pdwGeneration' , ), 1610678275, (1610678275, (), [ (16403, 0, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'GetWordsFromGenerationChange' , u'pdwGeneration' , u'pWordList' , ), 1610678276, (1610678276, (), [ (16403, 3, None, None) , 
			(36, 3, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetWords' , u'pdwGeneration' , u'pdwCookie' , u'pWordList' , ), 1610678277, (1610678277, (), [ 
			(16403, 3, None, None) , (16403, 3, None, None) , (36, 3, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'GetShortcutsForGeneration' , u'pdwGeneration' , u'pdwCookie' , u'pShortcutpairList' , ), 1610678278, (1610678278, (), [ 
			(16403, 3, None, None) , (16403, 3, None, None) , (36, 3, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetGenerationChange' , u'pdwGeneration' , u'pShortcutpairList' , ), 1610678279, (1610678279, (), [ (16403, 3, None, None) , 
			(36, 3, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISpStream_vtables_dispatch_ = 0
ISpStream_vtables_ = [
	(( u'SetBaseStream' , u'pStream' , u'rguidFormat' , u'pWaveFormatEx' , ), 1610874880, (1610874880, (), [ 
			(13, 0, None, "IID('{0000000C-0000-0000-C000-000000000046}')") , (36, 0, None, None) , (36, 0, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'GetBaseStream' , u'ppStream' , ), 1610874881, (1610874881, (), [ (16397, 0, None, "IID('{0000000C-0000-0000-C000-000000000046}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'BindToFile' , u'pszFileName' , u'eMode' , u'pFormatId' , u'pWaveFormatEx' , 
			u'ullEventInterest' , ), 1610874882, (1610874882, (), [ (31, 0, None, None) , (3, 0, None, None) , (36, 0, None, None) , 
			(36, 0, None, None) , (21, 0, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'Close' , ), 1610874883, (1610874883, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ISpStreamFormat_vtables_dispatch_ = 0
ISpStreamFormat_vtables_ = [
	(( u'GetFormat' , u'pguidFormatId' , u'ppCoMemWaveFormatEx' , ), 1610809344, (1610809344, (), [ (36, 0, None, None) , 
			(16420, 0, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISpStreamFormatConverter_vtables_dispatch_ = 0
ISpStreamFormatConverter_vtables_ = [
	(( u'SetBaseStream' , u'pStream' , u'fSetFormatToBaseStreamFormat' , u'fWriteToBaseStream' , ), 1610874880, (1610874880, (), [ 
			(13, 1, None, "IID('{BED530BE-2606-4F4D-A1C0-54C5CDA5566F}')") , (3, 1, None, None) , (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'GetBaseStream' , u'ppStream' , ), 1610874881, (1610874881, (), [ (16397, 2, None, "IID('{BED530BE-2606-4F4D-A1C0-54C5CDA5566F}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'SetFormat' , u'rguidFormatIdOfConvertedStream' , u'pWaveFormatExOfConvertedStream' , ), 1610874882, (1610874882, (), [ (36, 1, None, None) , 
			(36, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'ResetSeekPosition' , ), 1610874883, (1610874883, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'ScaleConvertedToBaseOffset' , u'ullOffsetConvertedStream' , u'pullOffsetBaseStream' , ), 1610874884, (1610874884, (), [ (21, 1, None, None) , 
			(16405, 2, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'ScaleBaseToConvertedOffset' , u'ullOffsetBaseStream' , u'pullOffsetConvertedStream' , ), 1610874885, (1610874885, (), [ (21, 1, None, None) , 
			(16405, 2, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

ISpVoice_vtables_dispatch_ = 0
ISpVoice_vtables_ = [
	(( u'SetOutput' , u'pUnkOutput' , u'fAllowFormatChanges' , ), 1610809344, (1610809344, (), [ (13, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'GetOutputObjectToken' , u'ppObjectToken' , ), 1610809345, (1610809345, (), [ (16397, 2, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'GetOutputStream' , u'ppStream' , ), 1610809346, (1610809346, (), [ (16397, 2, None, "IID('{BED530BE-2606-4F4D-A1C0-54C5CDA5566F}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Pause' , ), 1610809347, (1610809347, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'Resume' , ), 1610809348, (1610809348, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'SetVoice' , u'pToken' , ), 1610809349, (1610809349, (), [ (13, 1, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'GetVoice' , u'ppToken' , ), 1610809350, (1610809350, (), [ (16397, 2, None, "IID('{14056589-E16C-11D2-BB90-00C04F8EE6C0}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'Speak' , u'pwcs' , u'dwFlags' , u'pulStreamNumber' , ), 1610809351, (1610809351, (), [ 
			(31, 1, None, None) , (19, 1, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'SpeakStream' , u'pStream' , u'dwFlags' , u'pulStreamNumber' , ), 1610809352, (1610809352, (), [ 
			(13, 1, None, "IID('{0000000C-0000-0000-C000-000000000046}')") , (19, 1, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'GetStatus' , u'pStatus' , u'ppszLastBookmark' , ), 1610809353, (1610809353, (), [ (36, 2, None, None) , 
			(16415, 2, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'Skip' , u'pItemType' , u'lNumItems' , u'pulNumSkipped' , ), 1610809354, (1610809354, (), [ 
			(31, 1, None, None) , (3, 1, None, None) , (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'SetPriority' , u'ePriority' , ), 1610809355, (1610809355, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'GetPriority' , u'pePriority' , ), 1610809356, (1610809356, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'SetAlertBoundary' , u'eBoundary' , ), 1610809357, (1610809357, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'GetAlertBoundary' , u'peBoundary' , ), 1610809358, (1610809358, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'SetRate' , u'RateAdjust' , ), 1610809359, (1610809359, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'GetRate' , u'pRateAdjust' , ), 1610809360, (1610809360, (), [ (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'SetVolume' , u'usVolume' , ), 1610809361, (1610809361, (), [ (18, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'GetVolume' , u'pusVolume' , ), 1610809362, (1610809362, (), [ (16402, 2, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'WaitUntilDone' , u'msTimeout' , ), 1610809363, (1610809363, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( u'SetSyncSpeakTimeout' , u'msTimeout' , ), 1610809364, (1610809364, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( u'GetSyncSpeakTimeout' , u'pmsTimeout' , ), 1610809365, (1610809365, (), [ (16403, 2, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( u'SpeakCompleteEvent' , ), 1610809366, (1610809366, (), [ ], 1 , 1 , 4 , 0 , 280 , (16408, 0, None, None) , 0 , )),
	(( u'IsUISupported' , u'pszTypeOfUI' , u'pvExtraData' , u'cbExtraData' , u'pfSupported' , 
			), 1610809367, (1610809367, (), [ (31, 1, None, None) , (16408, 1, None, None) , (19, 1, None, None) , (16387, 2, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( u'DisplayUI' , u'hWndParent' , u'pszTitle' , u'pszTypeOfUI' , u'pvExtraData' , 
			u'cbExtraData' , ), 1610809368, (1610809368, (), [ (36, 1, None, None) , (31, 1, None, None) , (31, 1, None, None) , 
			(16408, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
]

ISpXMLRecoResult_vtables_dispatch_ = 0
ISpXMLRecoResult_vtables_ = [
	(( u'GetXMLResult' , u'ppszCoMemXMLResult' , u'Options' , ), 1610809344, (1610809344, (), [ (16415, 2, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'GetXMLErrorInfo' , u'pSemanticErrorInfo' , ), 1610809345, (1610809345, (), [ (36, 0, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ISpeechAudio_vtables_dispatch_ = 1
ISpeechAudio_vtables_ = [
	(( u'Status' , u'Status' , ), 200, (200, (), [ (16393, 10, None, "IID('{C62D9C91-7458-47F6-862D-1EF86FB0B278}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'BufferInfo' , u'BufferInfo' , ), 201, (201, (), [ (16393, 10, None, "IID('{11B103D8-1142-4EDF-A093-82FB3915F8CC}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'DefaultFormat' , u'StreamFormat' , ), 202, (202, (), [ (16393, 10, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Volume' , u'Volume' , ), 203, (203, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Volume' , u'Volume' , ), 203, (203, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'BufferNotifySize' , u'BufferNotifySize' , ), 204, (204, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'BufferNotifySize' , u'BufferNotifySize' , ), 204, (204, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'EventHandle' , u'EventHandle' , ), 205, (205, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( u'SetState' , u'State' , ), 206, (206, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 64 , )),
]

ISpeechAudioBufferInfo_vtables_dispatch_ = 1
ISpeechAudioBufferInfo_vtables_ = [
	(( u'MinNotification' , u'MinNotification' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'MinNotification' , u'MinNotification' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'BufferSize' , u'BufferSize' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'BufferSize' , u'BufferSize' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'EventBias' , u'EventBias' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'EventBias' , u'EventBias' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ISpeechAudioFormat_vtables_dispatch_ = 1
ISpeechAudioFormat_vtables_ = [
	(( u'Type' , u'AudioFormat' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Type' , u'AudioFormat' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Guid' , u'Guid' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 64 , )),
	(( u'Guid' , u'Guid' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
	(( u'GetWaveFormatEx' , u'WaveFormatEx' , ), 3, (3, (), [ (16393, 10, None, "IID('{7A1EF0D5-1581-4741-88E4-209A49F11A10}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 64 , )),
	(( u'SetWaveFormatEx' , u'WaveFormatEx' , ), 4, (4, (), [ (9, 1, None, "IID('{7A1EF0D5-1581-4741-88E4-209A49F11A10}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
]

ISpeechAudioStatus_vtables_dispatch_ = 1
ISpeechAudioStatus_vtables_ = [
	(( u'FreeBufferSpace' , u'FreeBufferSpace' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'NonBlockingIO' , u'NonBlockingIO' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'CurrentSeekPosition' , u'CurrentSeekPosition' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'CurrentDevicePosition' , u'CurrentDevicePosition' , ), 5, (5, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISpeechBaseStream_vtables_dispatch_ = 1
ISpeechBaseStream_vtables_ = [
	(( u'Format' , u'AudioFormat' , ), 1, (1, (), [ (16393, 10, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Format' , u'AudioFormat' , ), 1, (1, (), [ (9, 1, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 8 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Read' , u'Buffer' , u'NumberOfBytes' , u'BytesRead' , ), 2, (2, (), [ 
			(16396, 2, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Write' , u'Buffer' , u'BytesWritten' , ), 3, (3, (), [ (12, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Seek' , u'Position' , u'Origin' , u'NewPosition' , ), 4, (4, (), [ 
			(12, 1, None, None) , (3, 49, '0', None) , (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISpeechCustomStream_vtables_dispatch_ = 1
ISpeechCustomStream_vtables_ = [
	(( u'BaseStream' , u'ppUnkStream' , ), 100, (100, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'BaseStream' , u'ppUnkStream' , ), 100, (100, (), [ (13, 1, None, None) , ], 1 , 8 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISpeechDataKey_vtables_dispatch_ = 1
ISpeechDataKey_vtables_ = [
	(( u'SetBinaryValue' , u'ValueName' , u'Value' , ), 1, (1, (), [ (8, 1, None, None) , 
			(12, 1, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetBinaryValue' , u'ValueName' , u'Value' , ), 2, (2, (), [ (8, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'SetStringValue' , u'ValueName' , u'Value' , ), 3, (3, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetStringValue' , u'ValueName' , u'Value' , ), 4, (4, (), [ (8, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SetLongValue' , u'ValueName' , u'Value' , ), 5, (5, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'GetLongValue' , u'ValueName' , u'Value' , ), 6, (6, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'OpenKey' , u'SubKeyName' , u'SubKey' , ), 7, (7, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'CreateKey' , u'SubKeyName' , u'SubKey' , ), 8, (8, (), [ (8, 1, None, None) , 
			(16393, 10, None, "IID('{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'DeleteKey' , u'SubKeyName' , ), 9, (9, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'DeleteValue' , u'ValueName' , ), 10, (10, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'EnumKeys' , u'Index' , u'SubKeyName' , ), 11, (11, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'EnumValues' , u'Index' , u'ValueName' , ), 12, (12, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ISpeechFileStream_vtables_dispatch_ = 1
ISpeechFileStream_vtables_ = [
	(( u'Open' , u'FileName' , u'FileMode' , u'DoEvents' , ), 100, (100, (), [ 
			(8, 1, None, None) , (3, 49, '0', None) , (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Close' , ), 101, (101, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISpeechGrammarRule_vtables_dispatch_ = 1
ISpeechGrammarRule_vtables_ = [
	(( u'Attributes' , u'Attributes' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'InitialState' , u'State' , ), 2, (2, (), [ (16393, 10, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Name' , u'Name' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Id' , u'Id' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Clear' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AddResource' , u'ResourceName' , u'ResourceValue' , ), 6, (6, (), [ (8, 1, None, None) , 
			(8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AddState' , u'State' , ), 7, (7, (), [ (16393, 10, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISpeechGrammarRuleState_vtables_dispatch_ = 1
ISpeechGrammarRuleState_vtables_ = [
	(( u'Rule' , u'Rule' , ), 1, (1, (), [ (16393, 10, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Transitions' , u'Transitions' , ), 2, (2, (), [ (16393, 10, None, "IID('{EABCE657-75BC-44A2-AA7F-C56476742963}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AddWordTransition' , u'DestState' , u'Words' , u'Separators' , u'Type' , 
			u'PropertyName' , u'PropertyId' , u'PropertyValue' , u'Weight' , ), 3, (3, (), [ 
			(9, 1, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , (8, 1, None, None) , (8, 49, "u' '", None) , (3, 49, '1', None) , (8, 49, "u''", None) , 
			(3, 49, '0', None) , (16396, 49, "u''", None) , (4, 49, '1.0', None) , ], 1 , 1 , 4 , 0 , 72 , (3, 32, None, None) , 0 , )),
	(( u'AddRuleTransition' , u'DestinationState' , u'Rule' , u'PropertyName' , u'PropertyId' , 
			u'PropertyValue' , u'Weight' , ), 4, (4, (), [ (9, 1, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , (9, 1, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , 
			(8, 49, "u''", None) , (3, 49, '0', None) , (16396, 49, "u''", None) , (4, 49, '1.0', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 32, None, None) , 0 , )),
	(( u'AddSpecialTransition' , u'DestinationState' , u'Type' , u'PropertyName' , u'PropertyId' , 
			u'PropertyValue' , u'Weight' , ), 5, (5, (), [ (9, 1, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , (3, 1, None, None) , 
			(8, 49, "u''", None) , (3, 49, '0', None) , (16396, 49, "u''", None) , (4, 49, '1.0', None) , ], 1 , 1 , 4 , 0 , 88 , (3, 32, None, None) , 0 , )),
]

ISpeechGrammarRuleStateTransition_vtables_dispatch_ = 1
ISpeechGrammarRuleStateTransition_vtables_ = [
	(( u'Type' , u'Type' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Text' , u'Text' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Rule' , u'Rule' , ), 3, (3, (), [ (16393, 10, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Weight' , u'Weight' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'PropertyName' , u'PropertyName' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'PropertyId' , u'PropertyId' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'PropertyValue' , u'PropertyValue' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'NextState' , u'NextState' , ), 8, (8, (), [ (16393, 10, None, "IID('{D4286F2C-EE67-45AE-B928-28D695362EDA}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISpeechGrammarRuleStateTransitions_vtables_dispatch_ = 1
ISpeechGrammarRuleStateTransitions_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Transition' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ISpeechGrammarRules_vtables_dispatch_ = 1
ISpeechGrammarRules_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'FindRule' , u'RuleNameOrId' , u'Rule' , ), 6, (6, (), [ (12, 1, None, None) , 
			(16393, 10, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Rule' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 1 , )),
	(( u'Dynamic' , u'Dynamic' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Add' , u'RuleName' , u'Attributes' , u'RuleId' , u'Rule' , 
			), 3, (3, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , (16393, 10, None, "IID('{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Commit' , ), 4, (4, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'CommitAndSave' , u'ErrorText' , u'SaveStream' , ), 5, (5, (), [ (16392, 2, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISpeechLexicon_vtables_dispatch_ = 1
ISpeechLexicon_vtables_ = [
	(( u'GenerationId' , u'GenerationId' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 64 , )),
	(( u'GetWords' , u'Flags' , u'GenerationId' , u'Words' , ), 2, (2, (), [ 
			(3, 49, '3', None) , (16387, 50, '0', None) , (16393, 10, None, "IID('{8D199862-415E-47D5-AC4F-FAA608B424E6}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AddPronunciation' , u'bstrWord' , u'LangId' , u'PartOfSpeech' , u'bstrPronunciation' , 
			), 3, (3, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , (8, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 72 , (3, 32, None, None) , 0 , )),
	(( u'AddPronunciationByPhoneIds' , u'bstrWord' , u'LangId' , u'PartOfSpeech' , u'PhoneIds' , 
			), 4, (4, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , (16396, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 80 , (3, 32, None, None) , 64 , )),
	(( u'RemovePronunciation' , u'bstrWord' , u'LangId' , u'PartOfSpeech' , u'bstrPronunciation' , 
			), 5, (5, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , (8, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 88 , (3, 32, None, None) , 0 , )),
	(( u'RemovePronunciationByPhoneIds' , u'bstrWord' , u'LangId' , u'PartOfSpeech' , u'PhoneIds' , 
			), 6, (6, (), [ (8, 1, None, None) , (3, 1, None, None) , (3, 49, '0', None) , (16396, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 96 , (3, 32, None, None) , 64 , )),
	(( u'GetPronunciations' , u'bstrWord' , u'LangId' , u'TypeFlags' , u'ppPronunciations' , 
			), 7, (7, (), [ (8, 1, None, None) , (3, 49, '0', None) , (3, 49, '3', None) , (16393, 10, None, "IID('{72829128-5682-4704-A0D4-3E2BB6F2EAD3}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'GetGenerationChange' , u'GenerationId' , u'ppWords' , ), 8, (8, (), [ (16387, 3, None, None) , 
			(16393, 10, None, "IID('{8D199862-415E-47D5-AC4F-FAA608B424E6}')") , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
]

ISpeechLexiconPronunciation_vtables_dispatch_ = 1
ISpeechLexiconPronunciation_vtables_ = [
	(( u'Type' , u'LexiconType' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'LangId' , u'LangId' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'PartOfSpeech' , u'PartOfSpeech' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'PhoneIds' , u'PhoneIds' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Symbolic' , u'Symbolic' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISpeechLexiconPronunciations_vtables_dispatch_ = 1
ISpeechLexiconPronunciations_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Pronunciation' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{95252C5D-9E43-4F4A-9899-48EE73352F9F}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ISpeechLexiconWord_vtables_dispatch_ = 1
ISpeechLexiconWord_vtables_ = [
	(( u'LangId' , u'LangId' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Type' , u'WordType' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Word' , u'Word' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Pronunciations' , u'Pronunciations' , ), 4, (4, (), [ (16393, 10, None, "IID('{72829128-5682-4704-A0D4-3E2BB6F2EAD3}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISpeechLexiconWords_vtables_dispatch_ = 1
ISpeechLexiconWords_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Word' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ISpeechMMSysAudio_vtables_dispatch_ = 1
ISpeechMMSysAudio_vtables_ = [
	(( u'DeviceId' , u'DeviceId' , ), 300, (300, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'DeviceId' , u'DeviceId' , ), 300, (300, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'LineId' , u'LineId' , ), 301, (301, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'LineId' , u'LineId' , ), 301, (301, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'MMHandle' , u'Handle' , ), 302, (302, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
]

ISpeechMemoryStream_vtables_dispatch_ = 1
ISpeechMemoryStream_vtables_ = [
	(( u'SetData' , u'Data' , ), 100, (100, (), [ (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'GetData' , u'pData' , ), 101, (101, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

ISpeechObjectToken_vtables_dispatch_ = 1
ISpeechObjectToken_vtables_ = [
	(( u'Id' , u'ObjectId' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'DataKey' , u'DataKey' , ), 2, (2, (), [ (16393, 10, None, "IID('{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 64 , )),
	(( u'Category' , u'Category' , ), 3, (3, (), [ (16393, 10, None, "IID('{CA7EAC50-2D01-4145-86D4-5AE7D70F4469}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'GetDescription' , u'Locale' , u'Description' , ), 4, (4, (), [ (3, 49, '0', None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SetId' , u'Id' , u'CategoryID' , u'CreateIfNotExist' , ), 5, (5, (), [ 
			(8, 1, None, None) , (8, 49, "u''", None) , (11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 88 , (3, 32, None, None) , 64 , )),
	(( u'GetAttribute' , u'AttributeName' , u'AttributeValue' , ), 6, (6, (), [ (8, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'CreateInstance' , u'pUnkOuter' , u'ClsContext' , u'Object' , ), 7, (7, (), [ 
			(13, 49, 'None', None) , (3, 49, '23', None) , (16397, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Remove' , u'ObjectStorageCLSID' , ), 8, (8, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 64 , )),
	(( u'GetStorageFileName' , u'ObjectStorageCLSID' , u'KeyName' , u'FileName' , u'Folder' , 
			u'FilePath' , ), 9, (9, (), [ (8, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			(3, 1, None, None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 64 , )),
	(( u'RemoveStorageFileName' , u'ObjectStorageCLSID' , u'KeyName' , u'DeleteFile' , ), 10, (10, (), [ 
			(8, 1, None, None) , (8, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 64 , )),
	(( u'IsUISupported' , u'TypeOfUI' , u'ExtraData' , u'Object' , u'Supported' , 
			), 11, (11, (), [ (8, 1, None, None) , (16396, 49, "u''", None) , (13, 49, 'None', None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 32, None, None) , 64 , )),
	(( u'DisplayUI' , u'hWnd' , u'Title' , u'TypeOfUI' , u'ExtraData' , 
			u'Object' , ), 12, (12, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , 
			(16396, 49, "u''", None) , (13, 49, 'None', None) , ], 1 , 1 , 4 , 0 , 144 , (3, 32, None, None) , 64 , )),
	(( u'MatchesAttributes' , u'Attributes' , u'Matches' , ), 13, (13, (), [ (8, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ISpeechObjectTokenCategory_vtables_dispatch_ = 1
ISpeechObjectTokenCategory_vtables_ = [
	(( u'Id' , u'Id' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Default' , u'TokenId' , ), 2, (2, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Default' , u'TokenId' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'SetId' , u'Id' , u'CreateIfNotExist' , ), 3, (3, (), [ (8, 1, None, None) , 
			(11, 49, 'False', None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'GetDataKey' , u'Location' , u'DataKey' , ), 4, (4, (), [ (3, 49, '0', None) , 
			(16393, 10, None, "IID('{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 64 , )),
	(( u'EnumerateTokens' , u'RequiredAttributes' , u'OptionalAttributes' , u'Tokens' , ), 5, (5, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 32, None, None) , 0 , )),
]

ISpeechObjectTokens_vtables_dispatch_ = 1
ISpeechObjectTokens_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Token' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'ppEnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ISpeechPhoneConverter_vtables_dispatch_ = 1
ISpeechPhoneConverter_vtables_ = [
	(( u'LanguageId' , u'LanguageId' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'LanguageId' , u'LanguageId' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'PhoneToId' , u'Phonemes' , u'IdArray' , ), 2, (2, (), [ (8, 1, None, None) , 
			(16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'IdToPhone' , u'IdArray' , u'Phonemes' , ), 3, (3, (), [ (12, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISpeechPhraseAlternate_vtables_dispatch_ = 1
ISpeechPhraseAlternate_vtables_ = [
	(( u'RecoResult' , u'RecoResult' , ), 1, (1, (), [ (16393, 10, None, "IID('{ED2879CF-CED9-4EE6-A534-DE0191D5468D}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'StartElementInResult' , u'StartElement' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfElementsInResult' , u'NumberOfElements' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'PhraseInfo' , u'PhraseInfo' , ), 4, (4, (), [ (16393, 10, None, "IID('{961559CF-4E67-4662-8BF0-D93F1FCD61B3}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Commit' , ), 5, (5, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ISpeechPhraseAlternates_vtables_dispatch_ = 1
ISpeechPhraseAlternates_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'PhraseAlternate' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ISpeechPhraseElement_vtables_dispatch_ = 1
ISpeechPhraseElement_vtables_ = [
	(( u'AudioTimeOffset' , u'AudioTimeOffset' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'AudioSizeTime' , u'AudioSizeTime' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AudioStreamOffset' , u'AudioStreamOffset' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AudioSizeBytes' , u'AudioSizeBytes' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'RetainedStreamOffset' , u'RetainedStreamOffset' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'RetainedSizeBytes' , u'RetainedSizeBytes' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'DisplayText' , u'DisplayText' , ), 7, (7, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'LexicalForm' , u'LexicalForm' , ), 8, (8, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Pronunciation' , u'Pronunciation' , ), 9, (9, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'DisplayAttributes' , u'DisplayAttributes' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'RequiredConfidence' , u'RequiredConfidence' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'ActualConfidence' , u'ActualConfidence' , ), 12, (12, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'EngineConfidence' , u'EngineConfidence' , ), 13, (13, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ISpeechPhraseElements_vtables_dispatch_ = 1
ISpeechPhraseElements_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Element' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{E6176F96-E373-4801-B223-3B62C068C0B4}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ISpeechPhraseInfo_vtables_dispatch_ = 1
ISpeechPhraseInfo_vtables_ = [
	(( u'LanguageId' , u'LanguageId' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GrammarId' , u'GrammarId' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'StartTime' , u'StartTime' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AudioStreamPosition' , u'AudioStreamPosition' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'AudioSizeBytes' , u'pAudioSizeBytes' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'RetainedSizeBytes' , u'RetainedSizeBytes' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AudioSizeTime' , u'AudioSizeTime' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Rule' , u'Rule' , ), 8, (8, (), [ (16393, 10, None, "IID('{A7BFE112-A4A0-48D9-B602-C313843F6964}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Properties' , u'Properties' , ), 9, (9, (), [ (16393, 10, None, "IID('{08166B47-102E-4B23-A599-BDB98DBFD1F4}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Elements' , u'Elements' , ), 10, (10, (), [ (16393, 10, None, "IID('{0626B328-3478-467D-A0B3-D0853B93DDA3}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'Replacements' , u'Replacements' , ), 11, (11, (), [ (16393, 10, None, "IID('{38BC662F-2257-4525-959E-2069D2596C05}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'EngineId' , u'EngineIdGuid' , ), 12, (12, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'EnginePrivateData' , u'PrivateData' , ), 13, (13, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'SaveToMemory' , u'PhraseBlock' , ), 14, (14, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'GetText' , u'StartElement' , u'Elements' , u'UseReplacements' , u'Text' , 
			), 15, (15, (), [ (3, 49, '0', None) , (3, 49, '-1', None) , (11, 49, 'True', None) , (16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'GetDisplayAttributes' , u'StartElement' , u'Elements' , u'UseReplacements' , u'DisplayAttributes' , 
			), 16, (16, (), [ (3, 49, '0', None) , (3, 49, '-1', None) , (11, 49, 'True', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

ISpeechPhraseInfoBuilder_vtables_dispatch_ = 1
ISpeechPhraseInfoBuilder_vtables_ = [
	(( u'RestorePhraseFromMemory' , u'PhraseInMemory' , u'PhraseInfo' , ), 1, (1, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{961559CF-4E67-4662-8BF0-D93F1FCD61B3}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

ISpeechPhraseProperties_vtables_dispatch_ = 1
ISpeechPhraseProperties_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Property' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{CE563D48-961E-4732-A2E1-378A42B430BE}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ISpeechPhraseProperty_vtables_dispatch_ = 1
ISpeechPhraseProperty_vtables_ = [
	(( u'Name' , u'Name' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Id' , u'Id' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Value' , u'Value' , ), 3, (3, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'FirstElement' , u'FirstElement' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfElements' , u'NumberOfElements' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'EngineConfidence' , u'Confidence' , ), 6, (6, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Confidence' , u'Confidence' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Parent' , u'ParentProperty' , ), 8, (8, (), [ (16393, 10, None, "IID('{CE563D48-961E-4732-A2E1-378A42B430BE}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Children' , u'Children' , ), 9, (9, (), [ (16393, 10, None, "IID('{08166B47-102E-4B23-A599-BDB98DBFD1F4}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ISpeechPhraseReplacement_vtables_dispatch_ = 1
ISpeechPhraseReplacement_vtables_ = [
	(( u'DisplayAttributes' , u'DisplayAttributes' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Text' , u'Text' , ), 2, (2, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'FirstElement' , u'FirstElement' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfElements' , u'NumberOfElements' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISpeechPhraseReplacements_vtables_dispatch_ = 1
ISpeechPhraseReplacements_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Reps' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{2890A410-53A7-4FB5-94EC-06D4998E3D02}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ISpeechPhraseRule_vtables_dispatch_ = 1
ISpeechPhraseRule_vtables_ = [
	(( u'Name' , u'Name' , ), 1, (1, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Id' , u'Id' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'FirstElement' , u'FirstElement' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfElements' , u'NumberOfElements' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Parent' , u'Parent' , ), 5, (5, (), [ (16393, 10, None, "IID('{A7BFE112-A4A0-48D9-B602-C313843F6964}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Children' , u'Children' , ), 6, (6, (), [ (16393, 10, None, "IID('{9047D593-01DD-4B72-81A3-E4A0CA69F407}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Confidence' , u'ActualConfidence' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'EngineConfidence' , u'EngineConfidence' , ), 8, (8, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISpeechPhraseRules_vtables_dispatch_ = 1
ISpeechPhraseRules_vtables_ = [
	(( u'Count' , u'Count' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Item' , u'Index' , u'Rule' , ), 0, (0, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{A7BFE112-A4A0-48D9-B602-C313843F6964}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'_NewEnum' , u'EnumVARIANT' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ISpeechRecoContext_vtables_dispatch_ = 1
ISpeechRecoContext_vtables_ = [
	(( u'Recognizer' , u'Recognizer' , ), 1, (1, (), [ (16393, 10, None, "IID('{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'AudioInputInterferenceStatus' , u'Interference' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'RequestedUIType' , u'UIType' , ), 3, (3, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Voice' , u'Voice' , ), 4, (4, (), [ (9, 1, None, "IID('{269316D8-57BD-11D2-9EEE-00C04F797396}')") , ], 1 , 8 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Voice' , u'Voice' , ), 4, (4, (), [ (16393, 10, None, "IID('{269316D8-57BD-11D2-9EEE-00C04F797396}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AllowVoiceFormatMatchingOnNextSet' , u'pAllow' , ), 5, (5, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 64 , )),
	(( u'AllowVoiceFormatMatchingOnNextSet' , u'pAllow' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 64 , )),
	(( u'VoicePurgeEvent' , u'EventInterest' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'VoicePurgeEvent' , u'EventInterest' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'EventInterests' , u'EventInterest' , ), 7, (7, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'EventInterests' , u'EventInterest' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'CmdMaxAlternates' , u'MaxAlternates' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'CmdMaxAlternates' , u'MaxAlternates' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'RetainedAudio' , u'Option' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'RetainedAudio' , u'Option' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'RetainedAudioFormat' , u'Format' , ), 11, (11, (), [ (9, 1, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 8 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'RetainedAudioFormat' , u'Format' , ), 11, (11, (), [ (16393, 10, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'Pause' , ), 12, (12, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'Resume' , ), 13, (13, (), [ ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'CreateGrammar' , u'GrammarId' , u'Grammar' , ), 14, (14, (), [ (12, 49, '0', None) , 
			(16393, 10, None, "IID('{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'CreateResultFromMemory' , u'ResultBlock' , u'Result' , ), 15, (15, (), [ (16396, 1, None, None) , 
			(16393, 10, None, "IID('{ED2879CF-CED9-4EE6-A534-DE0191D5468D}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'Bookmark' , u'Options' , u'StreamPos' , u'BookmarkId' , ), 16, (16, (), [ 
			(3, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'SetAdaptationData' , u'AdaptationString' , ), 17, (17, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

ISpeechRecoGrammar_vtables_dispatch_ = 1
ISpeechRecoGrammar_vtables_ = [
	(( u'Id' , u'Id' , ), 1, (1, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'RecoContext' , u'RecoContext' , ), 2, (2, (), [ (16393, 10, None, "IID('{580AA49D-7E1E-4809-B8E2-57DA806104B8}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'Rules' , u'Rules' , ), 4, (4, (), [ (16393, 10, None, "IID('{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Reset' , u'NewLanguage' , ), 5, (5, (), [ (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromFile' , u'FileName' , u'LoadOption' , ), 7, (7, (), [ (8, 1, None, None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromObject' , u'ClassId' , u'GrammarName' , u'LoadOption' , ), 8, (8, (), [ 
			(8, 1, None, None) , (8, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromResource' , u'hModule' , u'ResourceName' , u'ResourceType' , u'LanguageId' , 
			u'LoadOption' , ), 9, (9, (), [ (3, 1, None, None) , (12, 1, None, None) , (12, 1, None, None) , 
			(3, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromMemory' , u'GrammarData' , u'LoadOption' , ), 10, (10, (), [ (12, 1, None, None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'CmdLoadFromProprietaryGrammar' , u'ProprietaryGuid' , u'ProprietaryString' , u'ProprietaryData' , u'LoadOption' , 
			), 11, (11, (), [ (8, 1, None, None) , (8, 1, None, None) , (12, 1, None, None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'CmdSetRuleState' , u'Name' , u'State' , ), 12, (12, (), [ (8, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'CmdSetRuleIdState' , u'RuleId' , u'State' , ), 13, (13, (), [ (3, 1, None, None) , 
			(3, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'DictationLoad' , u'TopicName' , u'LoadOption' , ), 14, (14, (), [ (8, 49, "u''", None) , 
			(3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 160 , (3, 32, None, None) , 0 , )),
	(( u'DictationUnload' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'DictationSetState' , u'State' , ), 16, (16, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'SetWordSequenceData' , u'Text' , u'TextLength' , u'Info' , ), 17, (17, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (9, 1, None, "IID('{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'SetTextSelection' , u'Info' , ), 18, (18, (), [ (9, 1, None, "IID('{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'IsPronounceable' , u'Word' , u'WordPronounceable' , ), 19, (19, (), [ (8, 1, None, None) , 
			(16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ISpeechRecoResult_vtables_dispatch_ = 1
ISpeechRecoResult_vtables_ = [
	(( u'RecoContext' , u'RecoContext' , ), 1, (1, (), [ (16393, 10, None, "IID('{580AA49D-7E1E-4809-B8E2-57DA806104B8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Times' , u'Times' , ), 2, (2, (), [ (16393, 10, None, "IID('{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AudioFormat' , u'Format' , ), 3, (3, (), [ (9, 1, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 8 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AudioFormat' , u'Format' , ), 3, (3, (), [ (16393, 10, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'PhraseInfo' , u'PhraseInfo' , ), 4, (4, (), [ (16393, 10, None, "IID('{961559CF-4E67-4662-8BF0-D93F1FCD61B3}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Alternates' , u'RequestCount' , u'StartElement' , u'Elements' , u'Alternates' , 
			), 5, (5, (), [ (3, 1, None, None) , (3, 49, '0', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Audio' , u'StartElement' , u'Elements' , u'Stream' , ), 6, (6, (), [ 
			(3, 49, '0', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{EEB14B68-808B-4ABE-A5EA-B51DA7588008}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'SpeakAudio' , u'StartElement' , u'Elements' , u'Flags' , u'StreamNumber' , 
			), 7, (7, (), [ (3, 49, '0', None) , (3, 49, '-1', None) , (3, 49, '0', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'SaveToMemory' , u'ResultBlock' , ), 8, (8, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'DiscardResultInfo' , u'ValueTypes' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

ISpeechRecoResult2_vtables_dispatch_ = 1
ISpeechRecoResult2_vtables_ = [
	(( u'SetTextFeedback' , u'Feedback' , u'WasSuccessful' , ), 12, (12, (), [ (8, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

ISpeechRecoResultDispatch_vtables_dispatch_ = 1
ISpeechRecoResultDispatch_vtables_ = [
	(( u'RecoContext' , u'RecoContext' , ), 1, (1, (), [ (16393, 10, None, "IID('{580AA49D-7E1E-4809-B8E2-57DA806104B8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Times' , u'Times' , ), 2, (2, (), [ (16393, 10, None, "IID('{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AudioFormat' , u'Format' , ), 3, (3, (), [ (9, 1, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 8 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AudioFormat' , u'Format' , ), 3, (3, (), [ (16393, 10, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'PhraseInfo' , u'PhraseInfo' , ), 4, (4, (), [ (16393, 10, None, "IID('{961559CF-4E67-4662-8BF0-D93F1FCD61B3}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Alternates' , u'RequestCount' , u'StartElement' , u'Elements' , u'Alternates' , 
			), 5, (5, (), [ (3, 1, None, None) , (3, 49, '0', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Audio' , u'StartElement' , u'Elements' , u'Stream' , ), 6, (6, (), [ 
			(3, 49, '0', None) , (3, 49, '-1', None) , (16393, 10, None, "IID('{EEB14B68-808B-4ABE-A5EA-B51DA7588008}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'SpeakAudio' , u'StartElement' , u'Elements' , u'Flags' , u'StreamNumber' , 
			), 7, (7, (), [ (3, 49, '0', None) , (3, 49, '-1', None) , (3, 49, '0', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'SaveToMemory' , u'ResultBlock' , ), 8, (8, (), [ (16396, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'DiscardResultInfo' , u'ValueTypes' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'GetXMLResult' , u'Options' , u'pResult' , ), 10, (10, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'GetXMLErrorInfo' , u'LineNumber' , u'ScriptLine' , u'Source' , u'Description' , 
			u'ResultCode' , u'IsError' , ), 11, (11, (), [ (16387, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'SetTextFeedback' , u'Feedback' , u'WasSuccessful' , ), 12, (12, (), [ (8, 1, None, None) , 
			(11, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

ISpeechRecoResultTimes_vtables_dispatch_ = 1
ISpeechRecoResultTimes_vtables_ = [
	(( u'StreamTime' , u'Time' , ), 1, (1, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Length' , u'Length' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'TickCount' , u'TickCount' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'OffsetFromStart' , u'OffsetFromStart' , ), 4, (4, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISpeechRecognizer_vtables_dispatch_ = 1
ISpeechRecognizer_vtables_ = [
	(( u'Recognizer' , u'Recognizer' , ), 1, (1, (), [ (9, 1, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Recognizer' , u'Recognizer' , ), 1, (1, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'AllowAudioInputFormatChangesOnNextSet' , u'Allow' , ), 2, (2, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 64 , )),
	(( u'AllowAudioInputFormatChangesOnNextSet' , u'Allow' , ), 2, (2, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 64 , )),
	(( u'AudioInput' , u'AudioInput' , ), 3, (3, (), [ (9, 49, '0', "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AudioInput' , u'AudioInput' , ), 3, (3, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AudioInputStream' , u'AudioInputStream' , ), 4, (4, (), [ (9, 49, '0', "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , ], 1 , 8 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'AudioInputStream' , u'AudioInputStream' , ), 4, (4, (), [ (16393, 10, None, "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'IsShared' , u'Shared' , ), 5, (5, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'State' , u'State' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'Status' , u'Status' , ), 7, (7, (), [ (16393, 10, None, "IID('{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'Profile' , u'Profile' , ), 8, (8, (), [ (9, 49, '0', "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'Profile' , u'Profile' , ), 8, (8, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'EmulateRecognition' , u'TextElements' , u'ElementDisplayAttributes' , u'LanguageId' , ), 9, (9, (), [ 
			(12, 1, None, None) , (16396, 49, "u''", None) , (3, 49, '0', None) , ], 1 , 1 , 4 , 0 , 168 , (3, 32, None, None) , 0 , )),
	(( u'CreateRecoContext' , u'NewContext' , ), 10, (10, (), [ (16393, 10, None, "IID('{580AA49D-7E1E-4809-B8E2-57DA806104B8}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'GetFormat' , u'Type' , u'Format' , ), 11, (11, (), [ (3, 1, None, None) , 
			(16393, 10, None, "IID('{E6E9C590-3E18-40E3-8299-061F98BDE7C7}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'SetPropertyNumber' , u'Name' , u'Value' , u'Supported' , ), 12, (12, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 64 , )),
	(( u'GetPropertyNumber' , u'Name' , u'Value' , u'Supported' , ), 13, (13, (), [ 
			(8, 1, None, None) , (16387, 3, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 64 , )),
	(( u'SetPropertyString' , u'Name' , u'Value' , u'Supported' , ), 14, (14, (), [ 
			(8, 1, None, None) , (8, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 64 , )),
	(( u'GetPropertyString' , u'Name' , u'Value' , u'Supported' , ), 15, (15, (), [ 
			(8, 1, None, None) , (16392, 3, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 64 , )),
	(( u'IsUISupported' , u'TypeOfUI' , u'ExtraData' , u'Supported' , ), 16, (16, (), [ 
			(8, 1, None, None) , (16396, 49, "u''", None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 32, None, None) , 0 , )),
	(( u'DisplayUI' , u'hWndParent' , u'Title' , u'TypeOfUI' , u'ExtraData' , 
			), 17, (17, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16396, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 232 , (3, 32, None, None) , 0 , )),
	(( u'GetRecognizers' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 18, (18, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 32, None, None) , 0 , )),
	(( u'GetAudioInputs' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 19, (19, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 32, None, None) , 0 , )),
	(( u'GetProfiles' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 20, (20, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 32, None, None) , 0 , )),
]

ISpeechRecognizerStatus_vtables_dispatch_ = 1
ISpeechRecognizerStatus_vtables_ = [
	(( u'AudioStatus' , u'AudioStatus' , ), 1, (1, (), [ (16393, 10, None, "IID('{C62D9C91-7458-47F6-862D-1EF86FB0B278}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'CurrentStreamPosition' , u'pCurrentStreamPos' , ), 2, (2, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'CurrentStreamNumber' , u'StreamNumber' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'NumberOfActiveRules' , u'NumberOfActiveRules' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'ClsidEngine' , u'ClsidEngine' , ), 5, (5, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SupportedLanguages' , u'SupportedLanguages' , ), 6, (6, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ISpeechResourceLoader_vtables_dispatch_ = 1
ISpeechResourceLoader_vtables_ = [
	(( u'LoadResource' , u'bstrResourceUri' , u'fAlwaysReload' , u'pStream' , u'pbstrMIMEType' , 
			u'pfModified' , u'pbstrRedirectUrl' , ), 1, (1, (), [ (8, 1, None, None) , (11, 1, None, None) , 
			(16397, 2, None, None) , (16392, 2, None, None) , (16395, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'GetLocalCopy' , u'bstrResourceUri' , u'pbstrLocalPath' , u'pbstrMIMEType' , u'pbstrRedirectUrl' , 
			), 2, (2, (), [ (8, 1, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , (16392, 2, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'ReleaseLocalCopy' , u'pbstrLocalPath' , ), 3, (3, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ISpeechTextSelectionInformation_vtables_dispatch_ = 1
ISpeechTextSelectionInformation_vtables_ = [
	(( u'ActiveOffset' , u'ActiveOffset' , ), 1, (1, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'ActiveOffset' , u'ActiveOffset' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'ActiveLength' , u'ActiveLength' , ), 2, (2, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'ActiveLength' , u'ActiveLength' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SelectionOffset' , u'SelectionOffset' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SelectionOffset' , u'SelectionOffset' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'SelectionLength' , u'SelectionLength' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'SelectionLength' , u'SelectionLength' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ISpeechVoice_vtables_dispatch_ = 1
ISpeechVoice_vtables_ = [
	(( u'Status' , u'Status' , ), 1, (1, (), [ (16393, 10, None, "IID('{8BE47B07-57F6-11D2-9EEE-00C04F797396}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Voice' , u'Voice' , ), 2, (2, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Voice' , u'Voice' , ), 2, (2, (), [ (9, 1, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'AudioOutput' , u'AudioOutput' , ), 3, (3, (), [ (16393, 10, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'AudioOutput' , u'AudioOutput' , ), 3, (3, (), [ (9, 1, None, "IID('{C74A3ADC-B727-4500-A84A-B526721C8B8C}')") , ], 1 , 8 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'AudioOutputStream' , u'AudioOutputStream' , ), 4, (4, (), [ (16393, 10, None, "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AudioOutputStream' , u'AudioOutputStream' , ), 4, (4, (), [ (9, 1, None, "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , ], 1 , 8 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'Rate' , u'Rate' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'Rate' , u'Rate' , ), 5, (5, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'Volume' , u'Volume' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'Volume' , u'Volume' , ), 6, (6, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'AllowAudioOutputFormatChangesOnNextSet' , u'Allow' , ), 7, (7, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 64 , )),
	(( u'AllowAudioOutputFormatChangesOnNextSet' , u'Allow' , ), 7, (7, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 64 , )),
	(( u'EventInterests' , u'EventInterestFlags' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( u'EventInterests' , u'EventInterestFlags' , ), 8, (8, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( u'Priority' , u'Priority' , ), 9, (9, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( u'Priority' , u'Priority' , ), 9, (9, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( u'AlertBoundary' , u'Boundary' , ), 10, (10, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( u'AlertBoundary' , u'Boundary' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( u'SynchronousSpeakTimeout' , u'msTimeout' , ), 11, (11, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( u'SynchronousSpeakTimeout' , u'msTimeout' , ), 11, (11, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( u'Speak' , u'Text' , u'Flags' , u'StreamNumber' , ), 12, (12, (), [ 
			(8, 1, None, None) , (3, 49, '0', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( u'SpeakStream' , u'Stream' , u'Flags' , u'StreamNumber' , ), 13, (13, (), [ 
			(9, 1, None, "IID('{6450336F-7D49-4CED-8097-49D6DEE37294}')") , (3, 49, '0', None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( u'Pause' , ), 14, (14, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( u'Resume' , ), 15, (15, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( u'Skip' , u'Type' , u'NumItems' , u'NumSkipped' , ), 16, (16, (), [ 
			(8, 1, None, None) , (3, 1, None, None) , (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( u'GetVoices' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 17, (17, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 32, None, None) , 0 , )),
	(( u'GetAudioOutputs' , u'RequiredAttributes' , u'OptionalAttributes' , u'ObjectTokens' , ), 18, (18, (), [ 
			(8, 49, "u''", None) , (8, 49, "u''", None) , (16393, 10, None, "IID('{9285B776-2E7B-4BC0-B53E-580EB6FA967F}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 32, None, None) , 0 , )),
	(( u'WaitUntilDone' , u'msTimeout' , u'Done' , ), 19, (19, (), [ (3, 1, None, None) , 
			(16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( u'SpeakCompleteEvent' , u'Handle' , ), 20, (20, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 64 , )),
	(( u'IsUISupported' , u'TypeOfUI' , u'ExtraData' , u'Supported' , ), 21, (21, (), [ 
			(8, 1, None, None) , (16396, 49, "u''", None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 32, None, None) , 0 , )),
	(( u'DisplayUI' , u'hWndParent' , u'Title' , u'TypeOfUI' , u'ExtraData' , 
			), 22, (22, (), [ (3, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , (16396, 49, "u''", None) , ], 1 , 1 , 4 , 0 , 304 , (3, 32, None, None) , 0 , )),
]

ISpeechVoiceStatus_vtables_dispatch_ = 1
ISpeechVoiceStatus_vtables_ = [
	(( u'CurrentStreamNumber' , u'StreamNumber' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'LastStreamNumberQueued' , u'StreamNumber' , ), 2, (2, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'LastHResult' , u'HResult' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'RunningState' , u'State' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'InputWordPosition' , u'Position' , ), 5, (5, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'InputWordLength' , u'Length' , ), 6, (6, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'InputSentencePosition' , u'Position' , ), 7, (7, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'InputSentenceLength' , u'Length' , ), 8, (8, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'LastBookmark' , u'Bookmark' , ), 9, (9, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'LastBookmarkId' , u'BookmarkId' , ), 10, (10, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 64 , )),
	(( u'PhonemeId' , u'PhoneId' , ), 11, (11, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'VisemeId' , u'VisemeId' , ), 12, (12, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ISpeechWaveFormatEx_vtables_dispatch_ = 1
ISpeechWaveFormatEx_vtables_ = [
	(( u'FormatTag' , u'FormatTag' , ), 1, (1, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'FormatTag' , u'FormatTag' , ), 1, (1, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Channels' , u'Channels' , ), 2, (2, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'Channels' , u'Channels' , ), 2, (2, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'SamplesPerSec' , u'SamplesPerSec' , ), 3, (3, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'SamplesPerSec' , u'SamplesPerSec' , ), 3, (3, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'AvgBytesPerSec' , u'AvgBytesPerSec' , ), 4, (4, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( u'AvgBytesPerSec' , u'AvgBytesPerSec' , ), 4, (4, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( u'BlockAlign' , u'BlockAlign' , ), 5, (5, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( u'BlockAlign' , u'BlockAlign' , ), 5, (5, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( u'BitsPerSample' , u'BitsPerSample' , ), 6, (6, (), [ (16386, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'BitsPerSample' , u'BitsPerSample' , ), 6, (6, (), [ (2, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( u'ExtraData' , u'ExtraData' , ), 7, (7, (), [ (16396, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( u'ExtraData' , u'ExtraData' , ), 7, (7, (), [ (12, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

ISpeechXMLRecoResult_vtables_dispatch_ = 1
ISpeechXMLRecoResult_vtables_ = [
	(( u'GetXMLResult' , u'Options' , u'pResult' , ), 10, (10, (), [ (3, 1, None, None) , 
			(16392, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( u'GetXMLErrorInfo' , u'LineNumber' , u'ScriptLine' , u'Source' , u'Description' , 
			u'ResultCode' , u'IsError' , ), 11, (11, (), [ (16387, 2, None, None) , (16392, 2, None, None) , 
			(16392, 2, None, None) , (16392, 2, None, None) , (16387, 2, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IStream_vtables_dispatch_ = 0
IStream_vtables_ = [
	(( u'RemoteSeek' , u'dlibMove' , u'dwOrigin' , u'plibNewPosition' , ), 1610743808, (1610743808, (), [ 
			(36, 1, None, None) , (19, 1, None, None) , (36, 2, None, None) , ], 1 , 1 , 4 , 0 , 40 , (3, 0, None, None) , 0 , )),
	(( u'SetSize' , u'libNewSize' , ), 1610743809, (1610743809, (), [ (36, 1, None, None) , ], 1 , 1 , 4 , 0 , 48 , (3, 0, None, None) , 0 , )),
	(( u'RemoteCopyTo' , u'pstm' , u'cb' , u'pcbRead' , u'pcbWritten' , 
			), 1610743810, (1610743810, (), [ (13, 1, None, "IID('{0000000C-0000-0000-C000-000000000046}')") , (36, 1, None, None) , (36, 2, None, None) , (36, 2, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( u'Commit' , u'grfCommitFlags' , ), 1610743811, (1610743811, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( u'Revert' , ), 1610743812, (1610743812, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( u'LockRegion' , u'libOffset' , u'cb' , u'dwLockType' , ), 1610743813, (1610743813, (), [ 
			(36, 1, None, None) , (36, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( u'UnlockRegion' , u'libOffset' , u'cb' , u'dwLockType' , ), 1610743814, (1610743814, (), [ 
			(36, 1, None, None) , (36, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( u'Stat' , u'pstatstg' , u'grfStatFlag' , ), 1610743815, (1610743815, (), [ (36, 2, None, None) , 
			(19, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( u'Clone' , u'ppstm' , ), 1610743816, (1610743816, (), [ (16397, 2, None, "IID('{0000000C-0000-0000-C000-000000000046}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
	###u'SPRULE': '{00000000-0000-0000-0000-000000000000}', # Record disabled because it doesn't have a non-null GUID
}

CLSIDToClassMap = {
	'{CFF8E175-019E-11D3-A08E-00C04F8EF9B5}' : ISpeechAudio,
	'{7013943A-E2EC-11D2-A086-00C04F8EF9B5}' : SpStreamFormatConverter,
	'{3BEE4890-4FE9-4A37-8C1E-5E7E12791C1F}' : SpSharedRecognizer,
	'{9185F743-1143-4C28-86B5-BFF14F20E5C8}' : SpPhoneConverter,
	'{7A1EF0D5-1581-4741-88E4-209A49F11A10}' : ISpeechWaveFormatEx,
	'{947812B3-2AE1-4644-BA86-9E90DED7EC91}' : SpFileStream,
	'{0F92030A-CBFD-4AB8-A164-FF5985547FF6}' : SpTextSelectionInformation,
	'{EABCE657-75BC-44A2-AA7F-C56476742963}' : ISpeechGrammarRuleStateTransitions,
	'{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}' : ISpeechGrammarRuleStateTransition,
	'{1A9E9F4F-104F-4DB8-A115-EFD7FD0C97AE}' : ISpeechCustomStream,
	'{41B89B6B-9399-11D2-9623-00C04F8EE628}' : SpInprocRecognizer,
	'{4F414126-DFE3-4629-99EE-797978317EAD}' : SpPhoneticAlphabetConverter,
	'{7B8FCB42-0E9D-4F00-A048-7B04D6179D3D}' : _ISpeechRecoContextEvents,
	'{9EF96870-E160-4792-820D-48CF0649E4EC}' : SpAudioFormat,
	'{9047D593-01DD-4B72-81A3-E4A0CA69F407}' : ISpeechPhraseRules,
	'{0D722F1A-9FCF-4E62-96D8-6DF8F01A26AA}' : SpShortcut,
	'{AF67F125-AB39-4E93-B4A2-CC2E66E182A7}' : ISpeechFileStream,
	'{0626B328-3478-467D-A0B3-D0853B93DDA3}' : ISpeechPhraseElements,
	'{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}' : ISpeechPhraseAlternate,
	'{715D9C59-4442-11D2-9605-00C04F8EE628}' : SpStream,
	'{269316D8-57BD-11D2-9EEE-00C04F797396}' : ISpeechVoice,
	'{6450336F-7D49-4CED-8097-49D6DEE37294}' : ISpeechBaseStream,
	'{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}' : ISpeechMMSysAudio,
	'{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}' : ISpeechLexiconWord,
	'{08166B47-102E-4B23-A599-BDB98DBFD1F4}' : ISpeechPhraseProperties,
	'{47206204-5ECA-11D2-960F-00C04F8EE628}' : SpSharedRecoContext,
	'{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}' : ISpeechRecoResultTimes,
	'{E6E9C590-3E18-40E3-8299-061F98BDE7C7}' : ISpeechAudioFormat,
	'{8E0A246D-D3C8-45DE-8657-04290C458C3C}' : ISpeechRecoResult2,
	'{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}' : ISpeechGrammarRule,
	'{D4286F2C-EE67-45AE-B928-28D695362EDA}' : ISpeechGrammarRuleState,
	'{E6176F96-E373-4801-B223-3B62C068C0B4}' : ISpeechPhraseElement,
	'{2890A410-53A7-4FB5-94EC-06D4998E3D02}' : ISpeechPhraseReplacement,
	'{8BE47B07-57F6-11D2-9EEE-00C04F797396}' : ISpeechVoiceStatus,
	'{38BC662F-2257-4525-959E-2069D2596C05}' : ISpeechPhraseReplacements,
	'{EF411752-3736-4CB4-9C8C-8EF4CCB58EFE}' : SpObjectToken,
	'{580AA49D-7E1E-4809-B8E2-57DA806104B8}' : ISpeechRecoContext,
	'{8DBEF13F-1948-4AA8-8CF0-048EEBED95D8}' : SpCustomStream,
	'{3DA7627A-C7AE-4B23-8708-638C50362C25}' : ISpeechLexicon,
	'{72829128-5682-4704-A0D4-3E2BB6F2EAD3}' : ISpeechLexiconPronunciations,
	'{AAEC54AF-8F85-4924-944D-B79D39D72E19}' : ISpeechXMLRecoResult,
	'{A8C680EB-3D32-11D2-9EE7-00C04F797396}' : SpMMAudioOut,
	'{C79A574C-63BE-44B9-801F-283F87F898BE}' : SpWaveFormatEx,
	'{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}' : ISpeechRecognizer,
	'{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}' : ISpeechGrammarRules,
	'{B9AC5783-FCD0-4B21-B119-B4F8DA8FD2C3}' : ISpeechResourceLoader,
	'{C9E37C15-DF92-4727-85D6-72E5EEB6995A}' : SpUnCompressedLexicon,
	'{C74A3ADC-B727-4500-A84A-B526721C8B8C}' : ISpeechObjectToken,
	'{CF3D2E50-53F2-11D2-960C-00C04F8EE628}' : SpMMAudioIn,
	'{ED2879CF-CED9-4EE6-A534-DE0191D5468D}' : ISpeechRecoResult,
	'{A910187F-0C7A-45AC-92CC-59EDAFB77B53}' : SpObjectTokenCategory,
	'{EEB14B68-808B-4ABE-A5EA-B51DA7588008}' : ISpeechMemoryStream,
	'{90903716-2F42-11D3-9C26-00C04F8EF87C}' : SpCompressedLexicon,
	'{CE563D48-961E-4732-A2E1-378A42B430BE}' : ISpeechPhraseProperty,
	'{73AD6842-ACE0-45E8-A4DD-8795881A2C2A}' : SpInProcRecoContext,
	'{9285B776-2E7B-4BC0-B53E-580EB6FA967F}' : ISpeechObjectTokens,
	'{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}' : ISpeechTextSelectionInformation,
	'{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}' : ISpeechPhraseAlternates,
	'{8D199862-415E-47D5-AC4F-FAA608B424E6}' : ISpeechLexiconWords,
	'{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}' : ISpeechRecoGrammar,
	'{A372ACD1-3BEF-4BBD-8FFB-CB3E2B416AF8}' : _ISpeechVoiceEvents,
	'{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}' : ISpeechRecognizerStatus,
	'{C62D9C91-7458-47F6-862D-1EF86FB0B278}' : ISpeechAudioStatus,
	'{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}' : ISpeechRecoResultDispatch,
	'{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}' : ISpeechDataKey,
	'{E2AE5372-5D40-11D2-960E-00C04F8EE628}' : SpNotifyTranslator,
	'{455F24E9-7396-4A16-9715-7C0FDBE3EFE3}' : SpNullPhoneConverter,
	'{95252C5D-9E43-4F4A-9899-48EE73352F9F}' : ISpeechLexiconPronunciation,
	'{CA7EAC50-2D01-4145-86D4-5AE7D70F4469}' : ISpeechObjectTokenCategory,
	'{C23FC28D-C55F-4720-8B32-91F73C2BD5D1}' : SpPhraseInfoBuilder,
	'{3B151836-DF3A-4E0A-846C-D2ADC9334333}' : ISpeechPhraseInfoBuilder,
	'{C3E4F353-433F-43D6-89A1-6A62A7054C3D}' : ISpeechPhoneConverter,
	'{AB1890A0-E91F-11D2-BB91-00C04F8EE6C0}' : SpMMAudioEnum,
	'{961559CF-4E67-4662-8BF0-D93F1FCD61B3}' : ISpeechPhraseInfo,
	'{0655E396-25D0-11D3-9C26-00C04F8EF87C}' : SpLexicon,
	'{A7BFE112-A4A0-48D9-B602-C313843F6964}' : ISpeechPhraseRule,
	'{96749373-3391-11D2-9EE3-00C04F797396}' : SpResourceManager,
	'{11B103D8-1142-4EDF-A093-82FB3915F8CC}' : ISpeechAudioBufferInfo,
	'{96749377-3391-11D2-9EE3-00C04F797396}' : SpVoice,
	'{5FB7EF7D-DFF4-468A-B6B7-2FCBD188F994}' : SpMemoryStream,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{CFF8E175-019E-11D3-A08E-00C04F8EF9B5}' : 'ISpeechAudio',
	'{5B4FB971-B115-4DE1-AD97-E482E3BF6EE4}' : 'ISpProperties',
	'{8FC6D974-C81E-4098-93C5-0147F61ED4D3}' : 'ISpRecognizer2',
	'{C05C768F-FAE8-4EC2-8E07-338321C12452}' : 'ISpAudio',
	'{7A1EF0D5-1581-4741-88E4-209A49F11A10}' : 'ISpeechWaveFormatEx',
	'{4B37BC9E-9ED6-44A3-93D3-18F022B79EC3}' : 'ISpRecoGrammar2',
	'{20B053BE-E235-43CD-9A2A-8D17A48B7842}' : 'ISpRecoResult',
	'{EABCE657-75BC-44A2-AA7F-C56476742963}' : 'ISpeechGrammarRuleStateTransitions',
	'{ACA16614-5D3D-11D2-960E-00C04F8EE628}' : 'ISpNotifyTranslator',
	'{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}' : 'ISpeechGrammarRuleStateTransition',
	'{1A9E9F4F-104F-4DB8-A115-EFD7FD0C97AE}' : 'ISpeechCustomStream',
	'{2D3D3845-39AF-4850-BBF9-40B49780011D}' : 'ISpObjectTokenCategory',
	'{BE7A9CC9-5F9E-11D2-960F-00C04F8EE628}' : 'ISpEventSink',
	'{B2745EFD-42CE-48CA-81F1-A96E02538A90}' : 'ISpPhoneticAlphabetSelection',
	'{BE7A9CCE-5F9E-11D2-960F-00C04F8EE628}' : 'ISpEventSource',
	'{DF1B943C-5838-4AA2-8706-D7CD5B333499}' : 'ISpRecognizer3',
	'{5EFF4AEF-8487-11D2-961C-00C04F8EE628}' : 'ISpNotifySource',
	'{9047D593-01DD-4B72-81A3-E4A0CA69F407}' : 'ISpeechPhraseRules',
	'{21B501A0-0EC7-46C9-92C3-A2BC784C54B9}' : 'ISpSerializeState',
	'{79EAC9ED-BAF9-11CE-8C82-00AA004BA90B}' : 'IInternetSecurityMgrSite',
	'{79EAC9EE-BAF9-11CE-8C82-00AA004BA90B}' : 'IInternetSecurityManager',
	'{15806F6E-1D70-4B48-98E6-3B1A007509AB}' : 'ISpMMSysAudio',
	'{AF67F125-AB39-4E93-B4A2-CC2E66E182A7}' : 'ISpeechFileStream',
	'{0626B328-3478-467D-A0B3-D0853B93DDA3}' : 'ISpeechPhraseElements',
	'{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}' : 'ISpeechPhraseAlternate',
	'{269316D8-57BD-11D2-9EEE-00C04F797396}' : 'ISpeechVoice',
	'{259684DC-37C3-11D2-9603-00C04F8EE628}' : 'ISpNotifySink',
	'{6450336F-7D49-4CED-8097-49D6DEE37294}' : 'ISpeechBaseStream',
	'{8FCEBC98-4E49-4067-9C6C-D86A0E092E3D}' : 'ISpPhraseAlt',
	'{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}' : 'ISpeechMMSysAudio',
	'{5B559F40-E952-11D2-BB91-00C04F8EE6C0}' : 'ISpObjectWithToken',
	'{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}' : 'ISpeechLexiconWord',
	'{133ADCD4-19B4-4020-9FDC-842E78253B17}' : 'ISpPhoneticAlphabetConverter',
	'{08166B47-102E-4B23-A599-BDB98DBFD1F4}' : 'ISpeechPhraseProperties',
	'{BEAD311C-52FF-437F-9464-6B21054CA73D}' : 'ISpRecoContext2',
	'{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}' : 'ISpeechRecoResultTimes',
	'{E6E9C590-3E18-40E3-8299-061F98BDE7C7}' : 'ISpeechAudioFormat',
	'{8E0A246D-D3C8-45DE-8657-04290C458C3C}' : 'ISpeechRecoResult2',
	'{0000000C-0000-0000-C000-000000000046}' : 'IStream',
	'{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}' : 'ISpeechGrammarRule',
	'{93384E18-5014-43D5-ADBB-A78E055926BD}' : 'ISpResourceManager',
	'{12E3CCA9-7518-44C5-A5E7-BA5A79CB929E}' : 'ISpStream',
	'{D4286F2C-EE67-45AE-B928-28D695362EDA}' : 'ISpeechGrammarRuleState',
	'{E6176F96-E373-4801-B223-3B62C068C0B4}' : 'ISpeechPhraseElement',
	'{2890A410-53A7-4FB5-94EC-06D4998E3D02}' : 'ISpeechPhraseReplacement',
	'{8137828F-591A-4A42-BE58-49EA7EBAAC68}' : 'ISpGrammarBuilder',
	'{1A5C0354-B621-4B5A-8791-D306ED379E53}' : 'ISpPhrase',
	'{8BE47B07-57F6-11D2-9EEE-00C04F797396}' : 'ISpeechVoiceStatus',
	'{38BC662F-2257-4525-959E-2069D2596C05}' : 'ISpeechPhraseReplacements',
	'{580AA49D-7E1E-4809-B8E2-57DA806104B8}' : 'ISpeechRecoContext',
	'{3DA7627A-C7AE-4B23-8708-638C50362C25}' : 'ISpeechLexicon',
	'{72829128-5682-4704-A0D4-3E2BB6F2EAD3}' : 'ISpeechLexiconPronunciations',
	'{AAEC54AF-8F85-4924-944D-B79D39D72E19}' : 'ISpeechXMLRecoResult',
	'{AE39362B-45A8-4074-9B9E-CCF49AA2D0B6}' : 'ISpXMLRecoResult',
	'{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}' : 'ISpeechRecognizer',
	'{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}' : 'ISpeechGrammarRules',
	'{C74A3ADC-B727-4500-A84A-B526721C8B8C}' : 'ISpeechObjectToken',
	'{C2B5F241-DAA0-4507-9E16-5A1EAA2B7A5C}' : 'ISpRecognizer',
	'{BED530BE-2606-4F4D-A1C0-54C5CDA5566F}' : 'ISpStreamFormat',
	'{ED2879CF-CED9-4EE6-A534-DE0191D5468D}' : 'ISpeechRecoResult',
	'{6C44DF74-72B9-4992-A1EC-EF996E0422D4}' : 'ISpVoice',
	'{EEB14B68-808B-4ABE-A5EA-B51DA7588008}' : 'ISpeechMemoryStream',
	'{CE563D48-961E-4732-A2E1-378A42B430BE}' : 'ISpeechPhraseProperty',
	'{9285B776-2E7B-4BC0-B53E-580EB6FA967F}' : 'ISpeechObjectTokens',
	'{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}' : 'ISpeechTextSelectionInformation',
	'{DA0CD0F9-14A2-4F09-8C2A-85CC48979345}' : 'ISpRecoCategory',
	'{3DF681E2-EA56-11D9-8BDE-F66BAD1E3F3A}' : 'ISpShortcut',
	'{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}' : 'ISpeechPhraseAlternates',
	'{8D199862-415E-47D5-AC4F-FAA608B424E6}' : 'ISpeechLexiconWords',
	'{6D5140C1-7436-11CE-8034-00AA006009FA}' : 'IServiceProvider',
	'{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}' : 'ISpeechRecoGrammar',
	'{06B64F9E-7FDA-11D2-B4F2-00C04F797396}' : 'IEnumSpObjectTokens',
	'{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}' : 'ISpeechRecognizerStatus',
	'{C62D9C91-7458-47F6-862D-1EF86FB0B278}' : 'ISpeechAudioStatus',
	'{2177DB29-7F45-47D0-8554-067E91C80502}' : 'ISpRecoGrammar',
	'{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}' : 'ISpeechRecoResultDispatch',
	'{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}' : 'ISpeechDataKey',
	'{95252C5D-9E43-4F4A-9899-48EE73352F9F}' : 'ISpeechLexiconPronunciation',
	'{CA7EAC50-2D01-4145-86D4-5AE7D70F4469}' : 'ISpeechObjectTokenCategory',
	'{8445C581-0CAC-4A38-ABFE-9B2CE2826455}' : 'ISpPhoneConverter',
	'{3B151836-DF3A-4E0A-846C-D2ADC9334333}' : 'ISpeechPhraseInfoBuilder',
	'{00000101-0000-0000-C000-000000000046}' : 'IEnumString',
	'{C3E4F353-433F-43D6-89A1-6A62A7054C3D}' : 'ISpeechPhoneConverter',
	'{0C733A30-2A1C-11CE-ADE5-00AA0044773D}' : 'ISequentialStream',
	'{678A932C-EA71-4446-9B41-78FDA6280A29}' : 'ISpStreamFormatConverter',
	'{961559CF-4E67-4662-8BF0-D93F1FCD61B3}' : 'ISpeechPhraseInfo',
	'{A7BFE112-A4A0-48D9-B602-C313843F6964}' : 'ISpeechPhraseRule',
	'{DA41A7C2-5383-4DB2-916B-6C1719E3DB58}' : 'ISpLexicon',
	'{11B103D8-1142-4EDF-A093-82FB3915F8CC}' : 'ISpeechAudioBufferInfo',
	'{14056581-E16C-11D2-BB90-00C04F8EE6C0}' : 'ISpDataKey',
	'{B9AC5783-FCD0-4B21-B119-B4F8DA8FD2C3}' : 'ISpeechResourceLoader',
	'{F740A62F-7C15-489E-8234-940A33D9272D}' : 'ISpRecoContext',
	'{14056589-E16C-11D2-BB90-00C04F8EE6C0}' : 'ISpObjectToken',
}


NamesToIIDMap = {
	'ISpeechRecoResult' : '{ED2879CF-CED9-4EE6-A534-DE0191D5468D}',
	'ISpRecoCategory' : '{DA0CD0F9-14A2-4F09-8C2A-85CC48979345}',
	'ISpeechPhraseProperties' : '{08166B47-102E-4B23-A599-BDB98DBFD1F4}',
	'ISpeechPhraseRules' : '{9047D593-01DD-4B72-81A3-E4A0CA69F407}',
	'ISpeechMemoryStream' : '{EEB14B68-808B-4ABE-A5EA-B51DA7588008}',
	'ISpeechAudioStatus' : '{C62D9C91-7458-47F6-862D-1EF86FB0B278}',
	'ISpEventSink' : '{BE7A9CC9-5F9E-11D2-960F-00C04F8EE628}',
	'ISpMMSysAudio' : '{15806F6E-1D70-4B48-98E6-3B1A007509AB}',
	'ISpeechGrammarRule' : '{AFE719CF-5DD1-44F2-999C-7A399F1CFCCC}',
	'ISpeechVoice' : '{269316D8-57BD-11D2-9EEE-00C04F797396}',
	'ISpNotifySink' : '{259684DC-37C3-11D2-9603-00C04F8EE628}',
	'ISpeechPhraseInfo' : '{961559CF-4E67-4662-8BF0-D93F1FCD61B3}',
	'ISpPhrase' : '{1A5C0354-B621-4B5A-8791-D306ED379E53}',
	'IEnumString' : '{00000101-0000-0000-C000-000000000046}',
	'ISpProperties' : '{5B4FB971-B115-4DE1-AD97-E482E3BF6EE4}',
	'ISpeechGrammarRuleState' : '{D4286F2C-EE67-45AE-B928-28D695362EDA}',
	'ISpeechPhraseReplacements' : '{38BC662F-2257-4525-959E-2069D2596C05}',
	'ISpeechAudio' : '{CFF8E175-019E-11D3-A08E-00C04F8EF9B5}',
	'ISpeechLexiconPronunciations' : '{72829128-5682-4704-A0D4-3E2BB6F2EAD3}',
	'ISpNotifyTranslator' : '{ACA16614-5D3D-11D2-960E-00C04F8EE628}',
	'ISpeechWaveFormatEx' : '{7A1EF0D5-1581-4741-88E4-209A49F11A10}',
	'ISpeechAudioBufferInfo' : '{11B103D8-1142-4EDF-A093-82FB3915F8CC}',
	'ISpRecognizer2' : '{8FC6D974-C81E-4098-93C5-0147F61ED4D3}',
	'ISpRecognizer3' : '{DF1B943C-5838-4AA2-8706-D7CD5B333499}',
	'ISpeechPhraseElement' : '{E6176F96-E373-4801-B223-3B62C068C0B4}',
	'IStream' : '{0000000C-0000-0000-C000-000000000046}',
	'ISpEventSource' : '{BE7A9CCE-5F9E-11D2-960F-00C04F8EE628}',
	'ISpRecoResult' : '{20B053BE-E235-43CD-9A2A-8D17A48B7842}',
	'ISpRecoGrammar2' : '{4B37BC9E-9ED6-44A3-93D3-18F022B79EC3}',
	'ISpeechRecoResultTimes' : '{62B3B8FB-F6E7-41BE-BDCB-056B1C29EFC0}',
	'ISpNotifySource' : '{5EFF4AEF-8487-11D2-961C-00C04F8EE628}',
	'ISpeechObjectTokens' : '{9285B776-2E7B-4BC0-B53E-580EB6FA967F}',
	'ISpRecognizer' : '{C2B5F241-DAA0-4507-9E16-5A1EAA2B7A5C}',
	'ISpRecoGrammar' : '{2177DB29-7F45-47D0-8554-067E91C80502}',
	'ISpeechRecoResult2' : '{8E0A246D-D3C8-45DE-8657-04290C458C3C}',
	'ISpObjectTokenCategory' : '{2D3D3845-39AF-4850-BBF9-40B49780011D}',
	'ISpStreamFormatConverter' : '{678A932C-EA71-4446-9B41-78FDA6280A29}',
	'ISpeechGrammarRules' : '{6FFA3B44-FC2D-40D1-8AFC-32911C7F1AD1}',
	'ISpeechLexiconWords' : '{8D199862-415E-47D5-AC4F-FAA608B424E6}',
	'IEnumSpObjectTokens' : '{06B64F9E-7FDA-11D2-B4F2-00C04F797396}',
	'ISpeechTextSelectionInformation' : '{3B9C7E7A-6EEE-4DED-9092-11657279ADBE}',
	'ISpPhoneticAlphabetSelection' : '{B2745EFD-42CE-48CA-81F1-A96E02538A90}',
	'ISpeechRecoGrammar' : '{B6D6F79F-2158-4E50-B5BC-9A9CCD852A09}',
	'ISpeechPhraseAlternate' : '{27864A2A-2B9F-4CB8-92D3-0D2722FD1E73}',
	'ISpeechMMSysAudio' : '{3C76AF6D-1FD7-4831-81D1-3B71D5A13C44}',
	'ISpeechRecoContext' : '{580AA49D-7E1E-4809-B8E2-57DA806104B8}',
	'ISpeechLexiconPronunciation' : '{95252C5D-9E43-4F4A-9899-48EE73352F9F}',
	'ISpeechPhraseReplacement' : '{2890A410-53A7-4FB5-94EC-06D4998E3D02}',
	'ISpeechGrammarRuleStateTransitions' : '{EABCE657-75BC-44A2-AA7F-C56476742963}',
	'ISpRecoContext2' : '{BEAD311C-52FF-437F-9464-6B21054CA73D}',
	'ISpPhoneConverter' : '{8445C581-0CAC-4A38-ABFE-9B2CE2826455}',
	'IInternetSecurityManager' : '{79EAC9EE-BAF9-11CE-8C82-00AA004BA90B}',
	'ISpLexicon' : '{DA41A7C2-5383-4DB2-916B-6C1719E3DB58}',
	'ISpeechRecognizer' : '{2D5F1C0C-BD75-4B08-9478-3B11FEA2586C}',
	'ISpeechPhoneConverter' : '{C3E4F353-433F-43D6-89A1-6A62A7054C3D}',
	'ISequentialStream' : '{0C733A30-2A1C-11CE-ADE5-00AA0044773D}',
	'ISpStream' : '{12E3CCA9-7518-44C5-A5E7-BA5A79CB929E}',
	'ISpeechLexiconWord' : '{4E5B933C-C9BE-48ED-8842-1EE51BB1D4FF}',
	'ISpRecoContext' : '{F740A62F-7C15-489E-8234-940A33D9272D}',
	'ISpeechVoiceStatus' : '{8BE47B07-57F6-11D2-9EEE-00C04F797396}',
	'ISpeechPhraseProperty' : '{CE563D48-961E-4732-A2E1-378A42B430BE}',
	'ISpeechPhraseRule' : '{A7BFE112-A4A0-48D9-B602-C313843F6964}',
	'ISpeechPhraseElements' : '{0626B328-3478-467D-A0B3-D0853B93DDA3}',
	'ISpPhoneticAlphabetConverter' : '{133ADCD4-19B4-4020-9FDC-842E78253B17}',
	'ISpeechCustomStream' : '{1A9E9F4F-104F-4DB8-A115-EFD7FD0C97AE}',
	'ISpStreamFormat' : '{BED530BE-2606-4F4D-A1C0-54C5CDA5566F}',
	'ISpeechXMLRecoResult' : '{AAEC54AF-8F85-4924-944D-B79D39D72E19}',
	'ISpeechPhraseAlternates' : '{B238B6D5-F276-4C3D-A6C1-2974801C3CC2}',
	'ISpShortcut' : '{3DF681E2-EA56-11D9-8BDE-F66BAD1E3F3A}',
	'ISpeechPhraseInfoBuilder' : '{3B151836-DF3A-4E0A-846C-D2ADC9334333}',
	'ISpPhraseAlt' : '{8FCEBC98-4E49-4067-9C6C-D86A0E092E3D}',
	'ISpGrammarBuilder' : '{8137828F-591A-4A42-BE58-49EA7EBAAC68}',
	'ISpVoice' : '{6C44DF74-72B9-4992-A1EC-EF996E0422D4}',
	'ISpDataKey' : '{14056581-E16C-11D2-BB90-00C04F8EE6C0}',
	'ISpXMLRecoResult' : '{AE39362B-45A8-4074-9B9E-CCF49AA2D0B6}',
	'ISpeechResourceLoader' : '{B9AC5783-FCD0-4B21-B119-B4F8DA8FD2C3}',
	'ISpeechObjectTokenCategory' : '{CA7EAC50-2D01-4145-86D4-5AE7D70F4469}',
	'ISpResourceManager' : '{93384E18-5014-43D5-ADBB-A78E055926BD}',
	'IInternetSecurityMgrSite' : '{79EAC9ED-BAF9-11CE-8C82-00AA004BA90B}',
	'ISpeechLexicon' : '{3DA7627A-C7AE-4B23-8708-638C50362C25}',
	'ISpeechAudioFormat' : '{E6E9C590-3E18-40E3-8299-061F98BDE7C7}',
	'ISpeechBaseStream' : '{6450336F-7D49-4CED-8097-49D6DEE37294}',
	'ISpeechRecognizerStatus' : '{BFF9E781-53EC-484E-BB8A-0E1B5551E35C}',
	'ISpeechDataKey' : '{CE17C09B-4EFA-44D5-A4C9-59D9585AB0CD}',
	'_ISpeechVoiceEvents' : '{A372ACD1-3BEF-4BBD-8FFB-CB3E2B416AF8}',
	'ISpeechRecoResultDispatch' : '{6D60EB64-ACED-40A6-BBF3-4E557F71DEE2}',
	'_ISpeechRecoContextEvents' : '{7B8FCB42-0E9D-4F00-A048-7B04D6179D3D}',
	'ISpeechGrammarRuleStateTransition' : '{CAFD1DB1-41D1-4A06-9863-E2E81DA17A9A}',
	'ISpObjectToken' : '{14056589-E16C-11D2-BB90-00C04F8EE6C0}',
	'IServiceProvider' : '{6D5140C1-7436-11CE-8034-00AA006009FA}',
	'ISpAudio' : '{C05C768F-FAE8-4EC2-8E07-338321C12452}',
	'ISpeechFileStream' : '{AF67F125-AB39-4E93-B4A2-CC2E66E182A7}',
	'ISpSerializeState' : '{21B501A0-0EC7-46C9-92C3-A2BC784C54B9}',
	'ISpObjectWithToken' : '{5B559F40-E952-11D2-BB91-00C04F8EE6C0}',
	'ISpeechObjectToken' : '{C74A3ADC-B727-4500-A84A-B526721C8B8C}',
}

win32com.client.constants.__dicts__.append(constants.__dict__)

